from repo_agent.chat_langchain.model import Model
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import  OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import LLMChain
from langchain_chroma import Chroma

import repo_agent.chat_langchain.utilities as utilities
#suppressing warnings
import warnings
import logging 

warnings.filterwarnings("ignore")
logging.getLogger().setLevel(logging.ERROR) # hide warning log
class ClassificationModel(Model):
    def __init__(self, path, path_hierarchy, model_name):
        super().__init__(path, path_hierarchy, model_name)
        self.history = []
        self.methods = self.get_methods_from_hierarchy()
        self.__set_contextualize_prompt()
        self.__set_classification_chain()

    def get_methods_from_hierarchy(self):
        methods = []
        for key in self.hierarchy.keys():
            for item in self.hierarchy[key]:
                methods.append(item["name"])
        return methods
    
    def get_classification(self,question):
        classification = self.classify_trough_name(question)
        # if the user is asking about a method then the question is specific 
        if self.classify_trough_name(question) == '\n specific':
            print("name-",classification)
            return classification, question
        
        refactored_question = self.__generate_standalone_question(question)
        
        response = self.chain.run(text=refactored_question).strip()
        print(response)
        return response, refactored_question

    
    def classify_trough_name(self,question):
        for method in self.methods:
            if method in question:
                return '\n specific'
        return ""
    
    def __set_contextualize_prompt(self):
      self.contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", utilities.get_contextualize_q_system_prompt()),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
        )
    

    def __generate_standalone_question(self, user_input):
        chain = LLMChain(llm=self.llm, prompt=self.contextualize_q_prompt)
        converted_history = convert_history(super().get_session_history("hist123"))
        standalone_question = chain.run(chat_history = converted_history, input=user_input)
        return standalone_question

    def __set_classification_chain(self):
        
        prompt_template = """
        You are a classifier that identifies general question in text. If the text matches the general examples, classify it as 'general'. If it doesn't match, classify it as 'specific'.

        Examples:
        general: "Explain me what the repository is about"
        general: "What is this program doing?"
        general: "How does the project work?"
        general: "What is the project about?"
        

        Classify the following text:
        Text: "{text}"
        Classification:
        """

        # Initialize the chain
        classifier = LLMChain(
            prompt=PromptTemplate.from_template(prompt_template),
            llm=self.llm
        )
            
        self.chain = classifier

def convert_history(history):
        new_history = []
        if len(history.messages) == 0:
            return []
        role = ["user", "system"] * int(len(history.messages)/2)
        for index, mess in enumerate(history.messages):
            new_history.append({"role": role[index], "content": mess.content})

        return new_history