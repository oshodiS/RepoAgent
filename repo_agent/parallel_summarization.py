import os
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain
from langchain.chains.summarize import load_summarize_chain, read_md_files
from chat_langchain.utilities import split_documents
import concurrent.futures


class Summarizator:
    def __init__(self, path, model_name):
        self.path = path
        self.llm = ChatOpenAI(temperature=0.1, model_name=model_name)
        self.docs = read_md_files(self.path)
        self.stuff_chain = self.get_stuff_chain()
        self.reduce_chain = self.get_reduce_chain()

    
    def get_stuff_chain(self):
        prompt_template = """Write a concise summary of the following:
        "{text}"
        CONCISE SUMMARY:"""
        prompt = PromptTemplate.from_template(prompt_template)

        llm_chain = LLMChain(llm=self.llm, prompt=prompt)

        # Define StuffDocumentsChain
        stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
        return stuff_chain
    
    def get_reduce_chain(self):
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
        return reduce_chain
    



    def get_parallel_summary(self, docs):
        def process_document_with_chain(doc):
            return self.stuff_chain.invoke([doc])["output_text"]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Map the process_document_with_chain function to the documents
            results = list(executor.map(process_document_with_chain, docs))

    
        return results


    def get_first_summarization(self):
        print(self.path)
        self.docs = read_md_files(self.path)
        summary = None
        if (len(self.docs) != 0):
            all_splits = []
            for doc in self.docs:
                    splits = split_documents(doc, 5000, 0)
                    for doc_split in splits:
                        filename = os.path.basename(list(doc.metadata.values())[0])
                        doc_split.metadata = {'source':filename}        
                    all_splits.extend(splits)
            single_summaries = self.get_parallel_summary(all_splits)
            summary = self.reduce_chain.invoke(single_summaries)["output_text"]

        return summary
        
   