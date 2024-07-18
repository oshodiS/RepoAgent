from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.runnables.history import RunnableWithMessageHistory

import repo_agent.chat_langchain.utilities as utilities
class Model:  
    store = {} #static 


    def __init__(self, path_marksdown, path_hierarchy, model_name):
        self.path_marksdown = path_marksdown
        self.llm = ChatOpenAI(temperature=0.1, model_name=model_name)
        #loader = DirectoryLoader(path, glob="./*.md", show_progress=True, loader_cls=UnstructuredMarkdownLoader)
        #docs = loader.load()
        self.docs = None
        self.prompt = None
        self.vectorstore = None
      
        self.chain = None
        self.hierarchy = utilities.get_json_from_path(path_hierarchy)

    def get_prompt(self):
        return self.prompt
    
    def set_vectorstore(self,  chunk_size, chunk_overlap, collection_name):
        summary_splits = utilities.get_chunk_with_source(self.docs, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        vectorstore = Chroma.from_documents(documents=summary_splits, embedding=OpenAIEmbeddings(), collection_name=collection_name)
        self.vectorstore = vectorstore
    
    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        max_messages = 3
        if session_id not in Model.store:
            Model.store[session_id] = ChatMessageHistory()
        
        old_messages = Model.store[session_id].messages
        if len(old_messages) > max_messages*2:
            Model.store[session_id].clear()
            c = 0 
            for message in old_messages[-2*(max_messages):]:
                if c % 2 == 0:
                    Model.store[session_id].add_user_message(message)
                else:
                    Model.store[session_id].add_ai_message(message)
                c += 1 
        return Model.store[session_id]

    
    
    def get_chain(self):
        return self.chain
    
    def create_chat_prompt(self, system_propmt):
        return ChatPromptTemplate.from_messages(
            [
                ("system", system_propmt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
    
    def create_runnable_chain(self, qa_prompt, history_prompt, retriever):

        contextualize_q_prompt = self.create_chat_prompt(history_prompt)
        history_aware_retriever = create_history_aware_retriever( self.llm, retriever, contextualize_q_prompt)
        qa_prompt = self.create_chat_prompt(qa_prompt)
        question_answer_chain = create_stuff_documents_chain(self.llm, qa_prompt)
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        return RunnableWithMessageHistory(
                        rag_chain,
                        self.get_session_history,
                        input_messages_key="input",
                        history_messages_key="chat_history",
                        output_messages_key="answer",
                    )
    
    def get_chunk_docs(self, chunk_size, chunk_overlap):
        summary_splits = utilities.get_chunk_with_source(self.docs, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return summary_splits
   
    def set_store(store, session_id):
        Model.store[session_id] = store
        