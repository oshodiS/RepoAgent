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
        self.__set_classification_prompt()

    def get_methods_from_hierarchy(self):
        methods = []
        for key in self.hierarchy.keys():
            for item in self.hierarchy[key]:
                methods.append(item["name"])
        return methods
    
    def get_classification(self,question):
        classification = self.classify_trought_name(question)
        # if the user is asking about a method then the question is specific 
        if self.classify_trought_name(question) == '\n specific':
            print("name-",classification)
            return classification
        
        refactored_question = self.__generate_standalone_question(question)
        response = self.prompt.format(input=refactored_question).strip()
        classification = response.split('\n')[0]
        print(classification)
        return "specific"

    
    def classify_trought_name(self,question):
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
    
    def __add_to_history(self, user_input, system_output, max_history_length=3):

        if len(self.history) >= 2*max_history_length:
            self.history.pop(0)
        self.history.append({"role": "user", "content": user_input})
        self.history.append({"role": "system", "content": system_output})
    
    def __generate_standalone_question(self, user_input):
        chain = LLMChain(llm=self.llm, prompt=self.contextualize_q_prompt)
        standalone_question = chain.run(chat_history = self.history, input=user_input)
        self.__add_to_history(user_input, standalone_question)
        return standalone_question

    def __set_classification_prompt(self):
        examples = [    
                        {
                            "question": "Explain me what the repository is about",
                            "answer": """general""",
                        },
                        {
                            "question": "What is this program doing?",
                            "answer": """general""",
                        },
                        {
                            "question": "How does the project work?",
                            "answer": """general""",
                        },
                        {
                            "question": "which parameter should be passed to the function?",
                            "answer": """specific""",
                        },
                        {
                            "question": "what does the function X returns?",
                            "answer": """specific""",
                        },
                        {
                            "question": "show me how to use function X",
                            "answer": """specific""",
                        },
                         {
                            "question": "explain the  function X",
                            "answer": """specific""",
                        },
                         {
                            "question": "explain the class X",
                            "answer": """specific""",
                        },
                        {
                            "question": "how the method X works?",
                            "answer": """specific""",
                        },
                         {
                            "question": "how the class X works?",
                            "answer": """specific""",
                        },
                        {
                            "question": """explain file X.md""",
                            "answer": """specific""",
                        },
                    ]
        example_prompt = PromptTemplate(
                            input_variables=["question", "answer"], template="{answer}"
                        )
        example_selector = SemanticSimilarityExampleSelector.from_examples(
                        examples,
                        OpenAIEmbeddings(),
                        Chroma,
                        k=1,
                    )
        prompt = FewShotPromptTemplate(
                    example_selector=example_selector,
                    example_prompt=example_prompt,
                    suffix="Question: {input}",
                    input_variables=["input"],
                    )
        self.prompt = prompt