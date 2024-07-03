from repo_agent.chat_langchain.model import *
from repo_agent.chat_langchain.model import Model
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader




class GeneralModel(Model):
    def __init__(self, path, path_hierarchy, model_name):
        super().__init__(path, path_hierarchy, model_name)
        self.template = """
                    Given the following context:
                    {context}
                    Provide a comprehensive overview of the project considering the question.
                   If the answer is not included in the provided information, do not answer the question and state, "I don't know"  """
        self.chain = None
        self.load_docs()
        super().set_vectorstore(1000, 100, "general-model")
        self.set_chain()

     
    def set_chain(self):
        contextualize_q_system_prompt = utilities.get_contextualize_q_system_prompt()
        general_retriever = self.vectorstore.as_retriever()
        self.chain = super().create_runnable_chain(contextualize_q_system_prompt, self.template, general_retriever)

    def load_docs(self):
        loader = DirectoryLoader(self.path, glob="./summary.md", show_progress=True, loader_cls=UnstructuredMarkdownLoader)
        docs = loader.load()
        self.docs = docs