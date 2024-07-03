from repo_agent.chat_langchain.general_model import GeneralModel
from repo_agent.chat_langchain.specific_model import SpecificModel
from repo_agent.chat_langchain.classification_model2 import ClassificationModel

class ChatRepo:
    def __init__(self, path, path_hierarchy, model_name, chunk_size, chunk_overlap):
        self.specific = SpecificModel(path, path_hierarchy, model_name, chunk_size, chunk_overlap)
        self.general = GeneralModel(path, path_hierarchy, model_name)
        self.classificator = ClassificationModel(path, path_hierarchy, model_name)
    
    def get_answer(self, question):
        classification = self.classificator.get_classification(question)
        if classification == 'general':
            response = self.general.get_chain().invoke({"input":question},
            config={
                "configurable": {"session_id": "gen123"}
            },  
            )["answer"]
        else:
            response = self.specific.get_chain().invoke({"input":question},
            config={
                "configurable": {"session_id": "spec123"}
            },  
            )["answer"]
        return response
    
    def start_chat(self):
        print("\n REPO CHAT \n")
        while True:
            question = input("Enter your question: ")
            if question == 'exit':
                break
            answer = self.get_answer(question)
            print("\n (me): ", question,"\n")
            print("\n (repo):",answer, "\n")