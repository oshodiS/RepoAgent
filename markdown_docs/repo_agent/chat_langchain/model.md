## ClassDef Model
**Model**: The function of Model is to provide a base class for different models used in the chat_langchain project.

**Attributes**:
- `store`: A static attribute that stores the session history for each session ID.
- `path_marksdown`: The path to the markdown file containing the chat history.
- `path_hierarchy`: The path to the JSON file containing the hierarchy information.
- `model_name`: The name of the model.

**Code Description**:
The `Model` class serves as a base class for other models used in the chat_langchain project. It contains several attributes and methods that are common to all models.

The `__init__` method initializes the `Model` object by setting the `path_marksdown`, `path_hierarchy`, and `model_name` attributes. It also initializes the `llm` attribute with an instance of the `ChatOpenAI` class. The `docs`, `prompt`, and `vectorstore` attributes are set to `None`, and the `chain` and `hierarchy` attributes are set using utility functions.

The `get_prompt` method returns the value of the `prompt` attribute.

The `set_vectorstore` method takes in `chunk_size`, `chunk_overlap`, and `collection_name` parameters. It splits the `docs` into chunks using the `utilities.get_chunk_with_source` function and creates a `vectorstore` using the `Chroma.from_documents` method. The `vectorstore` is then assigned to the `vectorstore` attribute.

The `get_session_history` method takes a `session_id` parameter and returns the session history for that session ID. If the session ID is not present in the `store`, a new `ChatMessageHistory` object is created and added to the `store`. If the length of the old messages exceeds twice the `max_messages` limit, the `ChatMessageHistory` object is cleared and only the last two messages are added to it.

The `get_chain` method returns the value of the `chain` attribute.

The `create_chat_prompt` method takes a `system_prompt` parameter and creates a chat prompt template using the `ChatPromptTemplate.from_messages` method. The template consists of a system prompt, a placeholder for chat history, and a placeholder for user input.

The `create_runnable_chain` method takes `qa_prompt`, `history_prompt`, and `retriever` parameters. It creates a contextualized question prompt using the `create_chat_prompt` method, creates a history-aware retriever using the `create_history_aware_retriever` function, and creates a question-answer chain and retrieval chain using utility functions. Finally, it returns a `RunnableWithMessageHistory` object with the retrieval chain, session history, and message keys.

The `get_chunk_docs` method takes `chunk_size` and `chunk_overlap` parameters and splits the `docs` into chunks using the `utilities.get_chunk_with_source` function. It returns the list of summary splits.

The `set_store` method takes `store` and `session_id` parameters and sets the session history for the given session ID in the `store` attribute.

**Note**: The `Model` class is designed to be a base class and should not be instantiated directly. It provides common functionality and attributes that can be used by subclasses.

**Output Example**:
```python
model = Model(path_marksdown="path/to/marksdown", path_hierarchy="path/to/hierarchy", model_name="model")
prompt = model.get_prompt()
model.set_vectorstore(chunk_size=1000, chunk_overlap=100, collection_name="collection")
session_history = model.get_session_history(session_id="session123")
chain = model.get_chain()
chat_prompt = model.create_chat_prompt(system_prompt="System prompt")
runnable_chain = model.create_runnable_chain(qa_prompt="QA prompt", history_prompt="History prompt", retriever=retriever)
chunk_docs = model.get_chunk_docs(chunk_size=100, chunk_overlap=50)
model.set_store(store, session_id="session123")
```
### FunctionDef __init__(self, path_marksdown, path_hierarchy, model_name)
**__init__**: The function of __init__ is to initialize the Model class with specific attributes and objects.

**parameters**:
- path_marksdown: A string representing the path for markdown files.
- path_hierarchy: A string representing the path for JSON hierarchy data.
- model_name: A string specifying the name of the model.

**Code Description**:
The __init__ function initializes the Model class by setting the path for markdown files, creating an instance of the ChatOpenAI class with specified parameters, and initializing attributes for storing documents, prompts, and vectors. It also initializes the chain and loads JSON hierarchy data using the get_json_from_path function from utilities.py.

The ChatOpenAI instance is created with a temperature of 0.1 and the provided model_name. The function get_json_from_path is used to load JSON data from the path_hierarchy file, which is then stored in the hierarchy attribute.

**Note**:
Ensure that the specified paths for markdown files and JSON hierarchy data are correct to prevent any file loading errors.
***
### FunctionDef get_prompt(self)
**get_prompt**: The function of get_prompt is to return the prompt stored in the object.

**parameters**: 
- self: The object itself.

**Code Description**: 
The get_prompt function is a method that retrieves and returns the prompt stored within the object it is called on. It does not take any external parameters and simply returns the value of the prompt attribute of the object.

**Note**: 
Developers can use this function to access the prompt data stored within the object and utilize it as needed in their code.

**Output Example**: 
If the prompt attribute of the object is "Please enter your name:", calling get_prompt() will return "Please enter your name:".
***
### FunctionDef set_vectorstore(self, chunk_size, chunk_overlap, collection_name)
**set_vectorstore**: The function of set_vectorstore is to prepare document chunks for vectorization using Chroma and assign the resulting vector store to the object.

**parameters**:
- chunk_size: The size of each chunk of text.
- chunk_overlap: The number of characters to overlap between chunks.
- collection_name: The name of the collection for the vector store.

**Code Description**:
The set_vectorstore function first splits the input documents into chunks using the get_chunk_with_source function from utilities.py. It then creates a vector store using Chroma from the document chunks and assigns it to the object's vectorstore attribute.

This function is utilized in the project by the __init__ method in the SpecificModel class to set up the vector store for a specific model based on the provided chunk size, chunk overlap, and collection name. Additionally, the __init__ method in the GeneralModel class also uses set_vectorstore to establish the vector store for a general model with predefined chunk size, overlap, and collection name.

**Note**:
- Ensure the chunk_size and chunk_overlap parameters are set appropriately for the desired chunking configuration.
- Provide a meaningful collection_name to identify the vector store for future reference.
***
### FunctionDef get_session_history(self, session_id)
**get_session_history**: The function of get_session_history is to retrieve the chat message history for a specific session ID, ensuring a maximum number of messages are maintained and handling message categorization based on the message index.

**parameters**:
- session_id (str): The unique identifier for the session.

**Code Description**:
The `get_session_history` function first checks if the session ID exists in the Model store. If not, it initializes a new ChatMessageHistory object for that session ID. It then retrieves the old messages from the Model store and checks if the number of messages exceeds twice the maximum allowed messages. If so, it clears the message history and categorizes the messages as user or AI messages based on the message index. Finally, it returns the updated chat message history for the session ID.

This function is crucial for maintaining and managing the chat message history for different sessions within the chatbot system. It ensures that the message history is appropriately managed and categorized based on the defined criteria.

**Note**:
Developers using this function should ensure that the session ID provided is valid and follows the expected format. Additionally, they should be aware of the message categorization logic based on the message index.

**Output Example**:
```
{
    "session_id": "hist123",
    "messages": [
        {
            "user": "Hello",
            "timestamp": "2022-01-01 12:00:00"
        },
        {
            "AI": "Hi there",
            "timestamp": "2022-01-01 12:01:00"
        },
        ...
    ]
}
```
***
### FunctionDef get_chain(self)
**get_chain**: The function of get_chain is to return the chain attribute of the object.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_chain function simply returns the chain attribute of the object it is called on.

In the project, the get_chain function is utilized in the get_answer method of the ChatRepo class. Depending on the classification of the question, either the general or specific chain is invoked to generate a response.

**Note**: Developers can use the get_chain function to access the chain attribute of the object and utilize it for further processing.

**Output Example**: 
If the chain attribute contains a list of strings representing a conversation history, calling get_chain would return something like:
["Hello, how can I assist you today?", "What is your query?", "Please provide more details for better assistance."]
***
### FunctionDef create_chat_prompt(self, system_propmt)
**create_chat_prompt**: The function of create_chat_prompt is to generate a chat prompt template based on the provided system prompt.

**parameters**:
- system_prompt: A string representing the system prompt to be included in the chat prompt template.

**Code Description**:
The `create_chat_prompt` function takes a system prompt as input and constructs a chat prompt template using the provided system prompt. The template includes the system prompt, a placeholder for chat history, and a placeholder for human input. The function utilizes the `ChatPromptTemplate.from_messages` method to create the template.

In the project, this function is called within the `create_runnable_chain` method in the context of building a runnable chain for a chatbot system. Specifically, it is used to create chat prompts for both the QA prompt and the history prompt, which are essential components of the chatbot's interaction flow. By incorporating the system prompt into the chat prompt template, the function contributes to the overall conversational logic of the chatbot.

**Note**:
Developers using this function should ensure that the system prompt provided is in the correct format and aligns with the intended conversational flow of the chatbot.

**Output Example**:
A sample output of the function may look like:
```
[
    ("system", system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
]
```
***
### FunctionDef create_runnable_chain(self, qa_prompt, history_prompt, retriever)
**create_runnable_chain**: The function of create_runnable_chain is to construct a chain of operations for a chatbot system, incorporating prompts and retrievers to facilitate question answering and conversation history management.

**parameters**:
- qa_prompt (str): The prompt for the question answering component.
- history_prompt (str): The prompt for managing conversation history.
- retriever: The retriever object responsible for fetching relevant information.

**Code Description**:
The create_runnable_chain function initializes a chat prompt for the question answering prompt and conversation history prompt. It then creates a history-aware retriever based on the provided retriever and contextualized question prompt. Subsequently, it constructs a chain of operations by creating a question-answer chain and a retrieval chain. Finally, it returns a RunnableWithMessageHistory object that encapsulates the constructed chain along with specific message keys for input, history, and output.

This function plays a crucial role in setting up the operational flow of the chatbot system by integrating prompts and retrievers to enable effective question answering and history management. It ensures a structured approach to handling user queries and maintaining a coherent conversation history.

**Note**:
Developers utilizing this function should ensure that the prompts and retriever provided align with the intended functionality of the chatbot system. Additionally, understanding the flow of information within the constructed chain is essential for proper system operation.

**Output Example**:
```
{
    "rag_chain": RagChain,
    "get_session_history": BaseChatMessageHistory,
    "input_messages_key": "input",
    "history_messages_key": "chat_history",
    "output_messages_key": "answer",
}
```
***
### FunctionDef get_chunk_docs(self, chunk_size, chunk_overlap)
**get_chunk_docs**: The function of get_chunk_docs is to split a list of documents into chunks of text with specified size and overlap, utilizing the get_chunk_with_source function.

**parameters**:
- chunk_size: The size of each chunk of text.
- chunk_overlap: The number of characters to overlap between chunks.

**Code Description**:
The get_chunk_docs function takes in the chunk_size and chunk_overlap parameters to split a list of documents into chunks of text. It internally calls the get_chunk_with_source function from utilities.py to perform the chunking operation. The get_chunk_with_source function splits the documents into chunks and assigns a source metadata to each chunk based on the document's filename. The function then aggregates all the splits and returns them as a single list of chunks.

In the project, the get_chunk_docs function is utilized in the SpecificModel class to prepare document chunks for further processing. Specifically, it is called in the show_chunk function in main.py to demonstrate how the documents are chunked and save the chunking results to a file for analysis.

**Note**:
- Ensure the chunk_size and chunk_overlap parameters are set according to the specific chunking requirements.
- The input documents should be structured appropriately for accurate chunking results.

**Output Example**:
```python
[
    Chunk 1: "Text chunk 1...",
    Chunk 2: "Text chunk 2...",
    ...
]
```
***
### FunctionDef set_store(store, session_id)
**set_store**: The function of set_store is to assign a store to a specific session ID in the Model.

**parameters**:
- store: The store to be assigned to the session ID.
- session_id: The unique identifier for the session.

**Code Description**:
The set_store function takes two parameters, store, and session_id. It then assigns the provided store to the Model under the specific session_id key.

**Note**:
It is important to ensure that the session_id provided is unique to avoid overwriting existing stores in the Model.
***
