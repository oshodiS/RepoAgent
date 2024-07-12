## ClassDef Model
**Model**: The function of Model is to provide a base class for different models used in the chat_langchain project.

**Attributes**:
- `path_marksdown`: The path to the markdown file.
- `path_hierarchy`: The path to the hierarchy file.
- `model_name`: The name of the model.
- `path_marksdown`: The path to the markdown file.
- `llm`: An instance of the ChatOpenAI class.
- `docs`: The loaded documents.
- `prompt`: The chat prompt template.
- `vectorstore`: The vector store for storing document embeddings.
- `chain`: The runnable chain for processing chat messages.
- `hierarchy`: The hierarchy information.

**Code Description**:
The `Model` class is a base class that provides common functionality for different models used in the chat_langchain project. It contains various methods for managing chat history, creating chat prompts, setting up vector stores, and creating runnable chains for processing chat messages.

The `__init__` method initializes the `Model` object with the provided parameters. It sets the `path_marksdown`, `path_hierarchy`, and `model_name` attributes. It also initializes the `llm` attribute with an instance of the `ChatOpenAI` class. The `docs`, `prompt`, `vectorstore`, and `chain` attributes are set to `None`, and the `hierarchy` attribute is set using the `utilities.get_json_from_path` method.

The `get_prompt` method returns the chat prompt template.

The `set_vectorstore` method sets the `vectorstore` attribute by splitting the loaded documents into chunks using the `utilities.get_chunk_with_source` method and creating a `Chroma` object with the OpenAI embeddings.

The `get_session_history` method retrieves the chat history for a given session ID. If the session does not exist, it creates a new `ChatMessageHistory` object and stores it in the `Model.store` dictionary.

The `get_chain` method returns the runnable chain for processing chat messages.

The `create_chat_prompt` method creates a chat prompt template using the provided system prompt and placeholders for the chat history and user input.

The `create_runnable_chain` method creates a runnable chain for processing chat messages. It takes a QA prompt, history prompt, and retriever as parameters. It creates a contextualized question prompt using the history prompt, creates a history-aware retriever using the provided retriever and contextualized question prompt, creates a QA prompt using the QA prompt parameter, and finally creates a runnable chain using the history-aware retriever and QA prompt.

The `get_chunk_docs` method splits the loaded documents into chunks using the `utilities.get_chunk_with_source` method and returns the resulting chunks.

The `set_store` method sets the session store in the `Model.store` dictionary.

**Note**: 
- The `Model` class is a base class and should not be instantiated directly. It is meant to be subclassed by specific models.
- The `Model.store` attribute is a static dictionary used to store chat histories for different sessions.

**Output Example**:
```python
model = Model(path_marksdown, path_hierarchy, model_name)
prompt = model.get_prompt()
model.set_vectorstore(chunk_size, chunk_overlap, collection_name)
session_history = model.get_session_history(session_id)
chain = model.get_chain()
chunk_docs = model.get_chunk_docs(chunk_size, chunk_overlap)
model.set_store(store, session_id)
```
### FunctionDef __init__(self, path_marksdown, path_hierarchy, model_name)
**__init__**: The function of __init__ is to initialize the Model class with specific attributes and load necessary data for the chat language chain model.

**parameters**:
- path_marksdown: A string representing the path to the markdown files.
- path_hierarchy: A string indicating the path to the JSON file containing hierarchy information.
- model_name: A string specifying the name of the model.

**Code Description**:
The __init__ function initializes the Model class by setting the path to markdown files, creating an instance of the ChatOpenAI class with defined parameters, and initializing attributes for storing documents, prompts, and vectors. It also initializes the chain and loads hierarchy information using the get_json_from_path function from utilities.py.

The ChatOpenAI instance is created with a temperature of 0.1 and the provided model name. The function also sets the initial values of docs, prompt, vectorstore, chain, and hierarchy to None.

The get_json_from_path function is used to load a JSON file from the specified path_hierarchy, which contains hierarchy information necessary for the model's operation.

**Note**:
Ensure that the path provided for path_hierarchy is a valid path to a JSON file. The function relies on the ChatOpenAI class and the get_json_from_path function from utilities.py to initialize the Model class successfully.
***
### FunctionDef get_prompt(self)
**get_prompt**: The function of get_prompt is to return the prompt stored in the object.

**parameters**: 
This Function does not take any parameters.

**Code Description**: 
The get_prompt function is a method of the Model class. When called, it retrieves and returns the prompt stored in the object using the self.prompt attribute.

**Note**: 
Developers can use this function to access the prompt data stored within the object instance.

**Output Example**: 
If the prompt stored in the object is "Please enter your message:", calling get_prompt() will return "Please enter your message:".
***
### FunctionDef set_vectorstore(self, chunk_size, chunk_overlap, collection_name)
**set_vectorstore**: The function of set_vectorstore is to create a vector store from a list of documents by splitting them into chunks and assigning a collection name.

**parameters**:
- chunk_size: The size of each chunk to split the documents.
- chunk_overlap: The number of characters to overlap between each chunk.
- collection_name: The name of the collection for the vector store.

**Code Description**:
The set_vectorstore function utilizes the get_chunk_with_source function from utilities.py to split the input documents into chunks with specified sizes and overlaps. It then creates a vector store using Chroma from the split documents, OpenAIEmbeddings, and the provided collection name. Finally, the function assigns the created vector store to the object's vectorstore attribute.

This function is called in the __init__ method of the SpecificModel class to set up the vector store for a specific model based on the given chunk size, overlap, and collection name. It plays a crucial role in preparing the data for further processing and retrieval tasks within the model.

**Note**:
- Ensure to adjust the chunk_size and chunk_overlap parameters according to the specific requirements of the model.
- Provide a meaningful collection name to differentiate the vector store for different models or purposes.
- Understanding the structure of the input documents is essential for accurate chunking and vector store creation.
***
### FunctionDef get_session_history(self, session_id)
**get_session_history**: The function of get_session_history is to retrieve the chat history for a specific session. If the session does not exist, it creates a new one.

**parameters**:
- session_id: A string representing the unique identifier of the session.

**Code Description**:
The get_session_history function checks if the provided session_id exists in the Model store. If the session does not exist, it creates a new ChatMessageHistory object and stores it in the Model. Finally, it returns the chat history associated with the session_id.

This function is crucial for managing chat session histories within the application. It ensures that each session has a corresponding chat history, allowing for seamless tracking and retrieval of past conversations.

**Relationship with Callers**:
The get_session_history function is called by other functions within the project, such as __generate_standalone_question and create_runnable_chain. In the context of __generate_standalone_question, the function is used to retrieve the chat history for a specific session and convert it for further processing. In create_runnable_chain, get_session_history is utilized to obtain the chat history for a session as part of creating a runnable chain for question answering.

**Note**:
Developers should ensure that the session_id provided is a valid string identifier for an existing or new session.

**Output Example**:
A ChatMessageHistory object representing the chat history for the specified session.
***
### FunctionDef get_chain(self)
**get_chain**: The function of get_chain is to return the chain attribute of the object.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_chain function simply returns the chain attribute of the object it is called on. This chain attribute likely holds some kind of data or functionality related to the object's purpose.

In the project, the get_chain function is called within the get_answer method of the ChatRepo class. Depending on the classification of the input question, either the general or specific chain is invoked with a modified question input. The get_chain function is used to retrieve the chain object associated with the general or specific category to further process the input question.

**Note**: Developers using this function should ensure that the chain attribute is appropriately initialized and populated before calling the get_chain function to avoid any potential errors.

**Output Example**: 
If the chain attribute contains a list of processing steps, invoking the get_chain function may return something like: 
['step1', 'step2', 'step3']
***
### FunctionDef create_chat_prompt(self, system_propmt)
**create_chat_prompt**: The function of create_chat_prompt is to generate a chat prompt template based on the provided system prompt.

**parameters**:
- system_prompt: A string representing the system prompt to be included in the chat prompt template.

**Code Description**:
The create_chat_prompt function takes a system prompt as input and creates a chat prompt template using ChatPromptTemplate.from_messages. The template includes the system prompt, a placeholder for chat history, and a placeholder for human input.

This function is called within the create_runnable_chain function in the project. In create_runnable_chain, create_chat_prompt is used to create contextualized question prompts and history-aware retrievers for a conversational chain. The output of create_chat_prompt contributes to building a runnable chain with message history for question answering and retrieval processes.

**Note**:
Ensure that the system prompt provided is in the correct format for inclusion in the chat prompt template.

**Output Example**:
```
{
    "system": "Welcome to the chat system.",
    "chat_history": MessagesPlaceholder object,
    "human": "{input}"
}
```
***
### FunctionDef create_runnable_chain(self, qa_prompt, history_prompt, retriever)
**create_runnable_chain**: The function of create_runnable_chain is to construct a chain for question answering with message history based on the provided question-answer prompt, history prompt, and retriever.

**parameters**:
- qa_prompt: A string representing the question-answer prompt.
- history_prompt: A string representing the history prompt.
- retriever: An object used for retrieving information.

**Code Description**:
The create_runnable_chain function initializes a contextualized question prompt, a history-aware retriever, a question-answer chain, and a retrieval chain. It then returns a RunnableWithMessageHistory object containing the constructed chain with specific message keys for input, chat history, and answer.

This function interacts with the get_session_history function to retrieve chat history and create_chat_prompt function to generate chat prompt templates. Additionally, it utilizes create_stuff_documents_chain and create_retrieval_chain functions to build the question-answer chain and retrieval chain, respectively.

**Note**:
Developers should ensure that the provided prompts and retriever are appropriate for question answering and retrieval processes.

**Output Example**:
```
RunnableWithMessageHistory(
    chain,
    chat_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)
```
***
### FunctionDef get_chunk_docs(self, chunk_size, chunk_overlap)
**get_chunk_docs**: The function of get_chunk_docs is to split a list of documents into chunks based on the specified chunk size and overlap parameters.

**parameters**:
- chunk_size: The size of each chunk.
- chunk_overlap: The number of characters to overlap between chunks.

**Code Description**:
The get_chunk_docs function utilizes the get_chunk_with_source function from utilities.py to split a list of documents into chunks. It passes the input documents along with the chunk size and overlap parameters to get_chunk_with_source, which then returns the split chunks with assigned source metadata. This function is essential for breaking down documents effectively for further processing within the Model class.

The get_chunk_docs function is called within the show_chunk function in main.py to demonstrate how the document is chunked. It creates an instance of SpecificModel, retrieves the chunking result by calling get_chunk_docs, and saves the chunking result to a file for further analysis. This function plays a crucial role in the chunking process within the project's workflow.

**Note**:
- Ensure to adjust the chunk_size and chunk_overlap parameters according to the desired chunking requirements.
- The output of get_chunk_docs is a list of document chunks for further processing or analysis.

**Output Example**:
```python
[
    Chunk 1,
    Chunk 2,
    ...
]
```
***
### FunctionDef set_store(store, session_id)
**set_store**: The function of set_store is to assign a store to a specific session ID in the Model.

**parameters**:
- store: Represents the store that will be assigned to the session ID.
- session_id: Represents the unique identifier of the session.

**Code Description**:
The set_store function takes two parameters, store, and session_id. It then assigns the provided store to the Model's store dictionary using the session_id as the key. This allows for storing and accessing the specific store associated with a particular session ID within the Model.

**Note**:
It is important to ensure that the session_id provided is unique to avoid overwriting existing stores associated with other session IDs.
***
