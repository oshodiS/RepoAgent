from repo_agent.chat_langchain.model import Model
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
import repo_agent.chat_langchain.utilities as utilities
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader

import os

class SpecificModel(Model):
    def __init__(self, path, path_hierarchy, model_name, chunk_size, chunk_overlap):
        super().__init__(path, path_hierarchy, model_name)
        self.docs = utilities.load_docs(path)
        super().set_vectorstore(chunk_size,chunk_overlap, "specific-model")
        
        self.metadata_field_info = [
                AttributeInfo(
                name='source',
                description="Filename and location of the source file", 
                type="string", 
                )]
        self.retriever = SelfQueryRetriever.from_llm(self.llm, 
                                                self.vectorstore, 
                                                "Code documentation", 
                                                self.metadata_field_info, 
                                                verbose=True,
                                                )
        self.set_chain()
        
    def set_chain(self):
        history_prompt = utilities.get_dont_contextualize_system_prompt()

        qa_system_prompt = utilities.get_qa_system_prompt()

        # Create Prompt Templates
        self.chain = super().create_runnable_chain(qa_system_prompt, history_prompt, self.retriever)




        # question_answer_chain = create_stuff_documents_chain(self.llm, qa_prompt)
        # history_aware_retriever = create_history_aware_retriever(
        #     self.llm, self.retriever, contextualize_q_prompt
        # )

        # rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

        # # Create Specific Chain with Message History Management
        # specific_chain = RunnableWithMessageHistory(
        #     rag_chain,
        #     super().get_session_history,
        #     input_messages_key="input",
        #     history_messages_key="chat_history",
        #     output_messages_key="answer",
        # )
        
        # self.chain = specific_chain

    def get_docs(self):
        return self.docs
  