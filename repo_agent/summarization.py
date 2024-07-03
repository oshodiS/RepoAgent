import os
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langchain import hub
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain

class Summarizator:
    def __init__(self, path, model_name):
        self.path = path
        self.llm = ChatOpenAI(temperature=0.1, model_name=model_name)
        self.docs = None
        self.map_reduce_chain = None


    
    def get_map_reduce_chain(self):

        map_template = """The following is a set of documents: {docs}
        Based on this list of documents, please make a short description of their contents.
        Helpful Answer:"""
        map_prompt = PromptTemplate.from_template(map_template)
        map_chain = LLMChain(llm=self.llm, prompt=map_prompt)

        # Reduce Template
        reduce_template = """The following is a set of summaries: {docs}
        Please distill these summaries into a final, consolidated summary of the overall contents. Ensure the final summary captures the main points and key details from each document.
        Helpful Answer:
        
        The standard format is as follows:

        # title: 
        ** Project Description:**  summary of the project

        Please note:
        - Write mainly in the desired language. If necessary, you can write with some english words in the analysis and description to enhance the document's readability because you do not need to translate the function name or variable name into the target language.

        """
        reduce_prompt = PromptTemplate.from_template(reduce_template)
        reduce_chain = LLMChain(llm=self.llm, prompt=reduce_prompt)

        # Run chain
        reduce_chain = LLMChain(llm=self.llm, prompt=reduce_prompt)

        # Takes a list of documents, combines them into a single string, and passes this to an LLMChain
        combine_documents_chain = StuffDocumentsChain(
            llm_chain=reduce_chain, document_variable_name="docs"
        )

        # Combines and iteratively reduces the mapped documents
        reduce_documents_chain = ReduceDocumentsChain(
            # This is final chain that is called.
            combine_documents_chain=combine_documents_chain,
            # If documents exceed context for `StuffDocumentsChain`
            collapse_documents_chain=combine_documents_chain,
            # The maximum number of tokens to group documents into.
            token_max=4000,
        )

        map_reduce_chain = MapReduceDocumentsChain(
                            # Map chain
                            llm_chain=map_chain,
                            # Reduce chain
                            reduce_documents_chain=reduce_documents_chain,
                            # The variable name in the llm_chain to put the documents in
                            document_variable_name="docs",
                            # Return the results of the map steps in the output
                            return_intermediate_steps=False,
                        )
        self.map_reduce_chain = map_reduce_chain
    
    def split_documents(self, doc, chunk_size, chunk_overlap):
        """ Split a document into chunks of text."""

        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]

        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on, strip_headers=False
        )
        md_header_splits = markdown_splitter.split_text( doc.page_content)
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )

        # Split
        splits = text_splitter.split_documents(md_header_splits)
    
        return splits
    
    def read_md_files(slef, root_path):
        all_docs = []
        for subdir, _, _ in os.walk(root_path):
            loader = DirectoryLoader(os.path.join(root_path, subdir), glob="./*.md", show_progress=True, loader_cls=UnstructuredMarkdownLoader)    
            docs = loader.load()
            all_docs.extend(docs)
        return all_docs



    def get_first_summarization(self):
        print(self.path)
        self.docs = self.read_md_files(self.path)
        summary = None
        if (len(self.docs) != 0):
            all_splits = []
            for doc in self.docs:
                    splits = self.split_documents(doc, 500, 0)
                    for doc_split in splits:
                        filename = os.path.basename(list(doc.metadata.values())[0])
                        doc_split.metadata = {'source':filename}        
                    all_splits.extend(splits)
            self.all_splits = all_splits
            self.get_map_reduce_chain()
            summary = self.map_reduce_chain.invoke(self.all_splits)["output_text"]
        return summary
         