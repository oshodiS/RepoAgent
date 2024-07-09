from repo_agent.chat_langchain.model import *
from repo_agent.chat_langchain.model import Model
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader




class GeneralModel(Model):
    def __init__(self, root, path_marksdown, path_hierarchy, model_name):
        super().__init__(path_marksdown, path_hierarchy, model_name)
        self.template = """
                    Given the following context:
                    {context}
                    Provide a comprehensive overview of the project considering the question.
                   If the answer is not included in the provided information, do not answer the question and state, "I don't know"  """
        self.chain = None
        self.root = root
        self.load_docs()
        super().set_vectorstore(1000, 100, "general-model")
        self.set_chain()

     
    def set_chain(self):
        prompt = utilities.get_dont_contextualize_system_prompt()
        general_retriever = self.vectorstore.as_retriever()
        self.chain = super().create_runnable_chain( self.template, prompt, general_retriever)

    def load_docs(self):
        readme_path = utilities.get_readme_path(self.root)
        if readme_path is None:
            loader = UnstructuredMarkdownLoader(self.path_marksdown/"summary.md", show_progress=True)
        else:
            loader = UnstructuredMarkdownLoader(readme_path, show_progress=True)
        docs = loader.load()
        self.docs = docs