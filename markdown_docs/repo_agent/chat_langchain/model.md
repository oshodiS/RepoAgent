## ClassDef Model
**Model**: The function of Model is to provide foundational functionalities for the chat language chain system.

**attributes**:
- path_marksdown: The path to the markdown files.
- path_hierarchy: The path to the hierarchy.
- model_name: The name of the model.
- path_marksdown: The path to the markdown files.
- llm: An instance of the ChatOpenAI class.
- docs: Holds the loaded documents.
- prompt: A chat prompt template for creating chat interactions.
- vectorstore: A vector store for storing document embeddings.
- chain: Represents the chat language chain.
- hierarchy: A JSON object representing the hierarchy.

**Code Description**:
The Model class serves as the foundation for the chat language chain system. It initializes with the path_marksdown, path_hierarchy, and model_name parameters. The path_marksdown parameter represents the path to the markdown files, while the path_hierarchy parameter represents the path to the hierarchy. The model_name parameter specifies the name of the model.

The class contains various methods to handle different functionalities within the chat language chain system. The __init__ method initializes the path_marksdown, path_hierarchy, and model_name attributes. It also initializes the llm attribute with an instance of the ChatOpenAI class.

The get_prompt method returns the prompt attribute, which is a chat prompt template for creating chat interactions. The set_vectorstore method sets up the vectorstore attribute by creating document embeddings using the Chroma.from_documents method.

The get_session_history method retrieves the chat history for a specific session. If the session does not exist, it creates a new session and adds it to the Model.store dictionary.

The get_chain method returns the chain attribute, which represents the chat language chain.

The create_chat_prompt method creates a chat prompt template for chat interactions. It takes a system_prompt as input and returns a ChatPromptTemplate object.

The create_runnable_chain method creates a runnable chain for chat interactions. It takes a qa_prompt, history_prompt, and retriever as input and returns a RunnableWithMessageHistory object.

The get_chunk_docs method retrieves document chunks based on the specified chunk_size and chunk_overlap parameters.

The set_store method sets the Model.store dictionary with a specific store and session_id.

The class plays a crucial role in the chat language chain system by providing foundational functionalities such as managing chat history, creating chat prompts, and setting up the chat language chain.

**Note**: When utilizing the Model class, ensure to provide the necessary parameters when initializing the class to enable its functionalities effectively.

**Output Example**:
```python
model = Model("path/to/markdown", "path/to/hierarchy", "model_name")
prompt = model.get_prompt()
model.set_vectorstore(1000, 100, "collection_name")
session_history = model.get_session_history("session_id")
chain = model.get_chain()
model.create_chat_prompt("system_prompt")
model.create_runnable_chain("qa_prompt", "history_prompt", retriever)
chunk_docs = model.get_chunk_docs(500, 50)
model.set_store(store, "session_id")
```
### FunctionDef __init__(self, path_marksdown, path_hierarchy, model_name)
**__init__**: The function of __init__ is to initialize the Model class with specific attributes and objects.

**parameters**:
- path_marksdown: A string representing the path for markdown files.
- path_hierarchy: A string representing the path for JSON hierarchy data.
- model_name: A string specifying the name of the model.

**Code Description**:
The __init__ function initializes the Model class by setting the path for markdown files, creating an instance of the ChatOpenAI class with defined parameters, and initializing attributes for storing documents, prompts, and vectors. It also initializes attributes for chain and hierarchy by calling utility functions.

Within the function, the ChatOpenAI instance is created with a temperature of 0.1 and the provided model_name. The loader and docs attributes are not initialized in this function but are commented out for potential future use. The chain attribute is set to None, and the hierarchy attribute is initialized by calling the get_json_from_path function from utilities.py with the path_hierarchy parameter.

**Note**:
Ensure that the path provided for markdown files and JSON hierarchy data is accurate to prevent any file handling errors. The function sets up the necessary components for the Model class to operate effectively.
***
### FunctionDef get_prompt(self)
**get_prompt**: The function of get_prompt is to return the prompt stored in the object.

**parameters**: 
- self: The object itself.

**Code Description**: 
The get_prompt function is a method that retrieves and returns the prompt value stored in the object it is called on.

**Note**: 
Developers can use this function to access the prompt value within the object and utilize it as needed in their code.

**Output Example**: 
If the prompt stored in the object is "Please enter your name:", calling get_prompt() will return "Please enter your name:".
***
### FunctionDef set_vectorstore(self, chunk_size, chunk_overlap, collection_name)
**set_vectorstore**: The function of set_vectorstore is to create a vector store for a list of documents by splitting them into chunks and assigning a collection name.

**parameters**:
- chunk_size: The size of each chunk for splitting the documents.
- chunk_overlap: The number of characters to overlap between consecutive chunks.
- collection_name: The name of the collection for the vector store.

**Code Description**:
The set_vectorstore function utilizes the get_chunk_with_source function to split the input list of documents into chunks based on the specified chunk size and overlap. It then creates a vector store using the Chroma library, OpenAIEmbeddings, and the provided collection name. Finally, the function assigns the created vector store to the object's vectorstore attribute for further use.

In the project structure, the set_vectorstore function is called within the Model class in the model.py file. It is invoked during the initialization of both the GeneralModel and SpecificModel classes to set up the vector store for general and specific models, respectively. The function plays a crucial role in preparing the data for downstream processing and retrieval tasks within the chat_langchain module.

**Note**:
- Ensure to adjust the chunk_size and chunk_overlap parameters according to the specific requirements of the document splitting process.
- Provide a meaningful collection name to distinguish different vector stores within the project.
- Understand the flow of data between the set_vectorstore function and its calling functions to maintain consistency in data processing operations.
***
### FunctionDef get_session_history(self, session_id)
**get_session_history**: The function of get_session_history is to retrieve the chat history for a specific session. If the session does not exist, it creates a new session and returns the chat history.

**parameters**:
- session_id: A string representing the unique identifier of the session.

**Code Description**:
The get_session_history function checks if the provided session_id exists in the Model's store. If the session does not exist, a new ChatMessageHistory object is created and stored in the Model's store with the session_id. Subsequently, the function returns the chat history associated with the session_id.

This function plays a crucial role in managing and accessing chat histories within the Model class, ensuring that the conversation context is maintained and updated as needed.

**Note**:
It is essential to provide a valid session_id when calling this function to retrieve or create the chat history for the corresponding session.

**Output Example**:
If the function is called with a session_id "session123", the output could be an instance of ChatMessageHistory containing the chat history for the session.
***
### FunctionDef get_chain(self)
**get_chain**: The function of get_chain is to return the chain attribute of the object.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_chain function simply returns the chain attribute of the object it is called on.

In the project, the get_chain function is utilized in the get_answer method of the ChatRepo class. Depending on the classification of the question provided, the get_answer method invokes the get_chain function of either the general or specific chain and retrieves the answer based on the input question and session configuration.

**Note**: It is important to ensure that the chain attribute is properly initialized before calling the get_chain function to avoid any potential errors.

**Output Example**: 
If the chain attribute contains a value "example_chain", calling get_chain will return "example_chain".
***
### FunctionDef create_chat_prompt(self, system_propmt)
**create_chat_prompt**: The function of create_chat_prompt is to generate a chat prompt template based on the provided system prompt.

**parameters**:
- system_prompt: A string representing the system prompt to be included in the chat prompt template.

**Code Description**:
The create_chat_prompt function takes a system prompt as input and constructs a chat prompt template using the ChatPromptTemplate class. The template includes the system prompt, a placeholder for chat history, and a placeholder for human input. The function then returns the constructed chat prompt template.

In the project, this function is called within the create_runnable_chain function in the same module. Specifically, it is used to create chat prompts for contextualizing questions and question-answer interactions within a runnable chain. The chat prompts are essential for setting up the message flow and structure of the conversation chain.

**Note**:
It is important to provide a valid system prompt as input to ensure the chat prompt template is constructed correctly.

**Output Example**:
A sample output of the create_chat_prompt function may look like:
```
ChatPromptTemplate.from_messages(
    [
        ("system", "Please provide your question."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
```
***
### FunctionDef create_runnable_chain(self, qa_prompt, history_prompt, retriever)
**create_runnable_chain**: The function of create_runnable_chain is to construct a runnable chain for processing chat messages by setting up various components such as prompts and retrievers.

**parameters**:
- qa_prompt: A string representing the prompt for question-answer interactions.
- history_prompt: A string representing the prompt for contextualizing chat history.
- retriever: An object used for retrieving information.

**Code Description**:
The create_runnable_chain function first creates a contextualized question prompt using the create_chat_prompt method. It then generates a history-aware retriever by combining the language model, retriever, and contextualized question prompt. Subsequently, it creates prompts for question-answer interactions and constructs a retrieval chain. Finally, the function returns a RunnableWithMessageHistory object containing the constructed chain along with specific message keys for input, chat history, and answer.

This function is essential for establishing a structured flow within the chat processing chain, ensuring effective handling of chat messages. It is called within the Model class to set up the necessary components for processing chat interactions seamlessly.

**Note**:
- Ensure valid prompts and retriever objects are provided to create a functional runnable chain.
- The function encapsulates the logic for creating a chain of components required for processing chat messages efficiently.

**Output Example**:
A possible output of the create_runnable_chain function could be a RunnableWithMessageHistory object containing the configured chat message processing chain with designated message keys.
***
### FunctionDef get_chunk_docs(self, chunk_size, chunk_overlap)
**get_chunk_docs**: The function of get_chunk_docs is to split a list of documents into chunks of text with specified size and overlap, utilizing the get_chunk_with_source function from utilities.py.

**parameters**:
- chunk_size: The size of each chunk to be created.
- chunk_overlap: The number of characters to overlap between consecutive chunks.

**Code Description**:
The get_chunk_docs function takes the input list of documents and calls the get_chunk_with_source function to split the documents into chunks based on the provided chunk size and overlap parameters. The function then returns the split chunks with assigned source metadata.

In the project, the get_chunk_docs function is called within the show_chunk function in main.py. The show_chunk function is responsible for displaying how the document is chunked and saving the chunking result to a file. By utilizing get_chunk_docs, the show_chunk function generates and saves the chunked content of the documents for further processing or analysis.

**Note**:
- Ensure the chunk_size and chunk_overlap parameters are set appropriately to control the size and overlap of the text chunks.
- The output of get_chunk_docs can be further processed or saved for analysis or storage purposes.

**Output Example**:
```
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
- session_id: Represents the unique identifier of the session where the store will be stored.

**Code Description**:
The set_store function takes two parameters, store, and session_id. It then assigns the provided store to the Model under the specific session_id key. This allows for easy retrieval of the store based on the associated session ID.

**Note**:
It is important to ensure that the session_id provided is unique to avoid overwriting existing stores associated with other session IDs.
***
