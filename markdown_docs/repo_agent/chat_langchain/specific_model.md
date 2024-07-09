## ClassDef SpecificModel
**SpecificModel**: The SpecificModel class is responsible for handling specific functionalities within the chat language chain system.

**attributes**:
- path: The path to the markdown files.
- path_hierarchy: The path to the hierarchy.
- model_name: The name of the model.
- chunk_size: The size of the document chunks.
- chunk_overlap: The overlap between document chunks.
- metadata_field_info: A list of AttributeInfo objects representing metadata field information.
- retriever: An instance of the SelfQueryRetriever class.
- chain: Represents the chat language chain.
- docs: Holds the loaded documents.

**Code Description**:
The SpecificModel class is a subclass of the Model class and inherits its attributes and methods. It initializes with the path, path_hierarchy, model_name, chunk_size, and chunk_overlap parameters. The path parameter represents the path to the markdown files, while the path_hierarchy parameter represents the path to the hierarchy. The model_name parameter specifies the name of the model. The chunk_size and chunk_overlap parameters determine the size and overlap of the document chunks.

The class contains several methods to handle specific functionalities within the chat language chain system. The load_docs method loads the markdown documents from the specified path and stores them in the docs attribute.

The get_docs method returns the loaded documents.

The set_chain method sets up the chat language chain by creating prompt templates and a runnable chain. It initializes the history_prompt and qa_system_prompt variables using utility functions. It then creates a prompt template for chat interactions using the create_chat_prompt method inherited from the Model class. Finally, it creates a runnable chain by calling the create_runnable_chain method inherited from the Model class.

The load_docs and set_chain methods are called in the __init__ method to ensure that the documents are loaded and the chat language chain is set up when an instance of the SpecificModel class is created.

The SpecificModel class plays a crucial role in the chat language chain system by handling specific functionalities such as loading documents, setting up the chat language chain, and providing access to the loaded documents.

**Note**: When utilizing the SpecificModel class, ensure to provide the necessary parameters when initializing the class to enable its functionalities effectively.

**Output Example**:
```python
specific_model = SpecificModel("path/to/markdown", "path/to/hierarchy", "model_name", 1000, 100)
specific_model.load_docs()
docs = specific_model.get_docs()
specific_model.set_chain()
```
### FunctionDef __init__(self, path, path_hierarchy, model_name, chunk_size, chunk_overlap)
**__init__**: The function of __init__ is to initialize the SpecificModel object by setting up the necessary attributes, loading documents from a specified directory, configuring a vector store, creating a retriever object, and establishing a chat message processing chain.

**parameters**:
- path: The path to the directory containing the documents.
- path_hierarchy: The hierarchy of paths within the directory.
- model_name: The name of the model.
- chunk_size: The size of each chunk for document splitting.
- chunk_overlap: The number of characters to overlap between consecutive chunks.

**Code Description**:
The __init__ function first calls the parent class's initialization method to set the path, path_hierarchy, and model_name attributes. It then loads the documents from the specified path using the load_docs method. Next, it configures the vector store by calling the set_vectorstore method inherited from the Model class, passing the chunk_size, chunk_overlap, and a specific collection name. 

Following this, the function initializes metadata_field_info with information about the 'source' attribute. It then creates a retriever object using SelfQueryRetriever.from_llm, providing the necessary parameters such as the llm model, vectorstore, metadata field information, and verbosity setting. Finally, the function sets up the chat message processing chain by calling the set_chain method.

In the project structure, the __init__ function is a crucial part of initializing the SpecificModel class within the chat_langchain module. It orchestrates the setup of document loading, vector store configuration, retriever creation, and chat message processing chain establishment. By executing these steps, the function prepares the SpecificModel object for handling chat messages effectively within the defined model context.

**Note**:
- Ensure to provide valid paths and model names when initializing the SpecificModel object.
- Adjust the chunk_size and chunk_overlap parameters based on the desired document splitting configuration.
- Understand the sequence of operations within the __init__ function to grasp the overall setup process of the SpecificModel class for chat message processing.
***
### FunctionDef set_chain(self)
**set_chain**: The function of set_chain is to establish a chat message processing chain by creating prompt templates for question-answer interactions and chat history, and then constructing a retrieval chain using these prompts along with a retriever object.

**parameters**:
- This function does not take any parameters.

**Code Description**:
The set_chain function first retrieves a system prompt for chat history from the get_dont_contextualize_system_prompt function and a prompt for question-answer interactions from the get_qa_system_prompt function. It then utilizes the create_runnable_chain function from the Model class to generate a runnable chain incorporating the retrieved prompts and the retriever object. By doing so, it sets up a structured flow within the chat processing chain, ensuring effective handling of chat messages within the SpecificModel context.

This function is called within the __init__ method of the SpecificModel class to initialize the chat message processing chain along with other essential components such as document loading, vector store configuration, and retriever creation. The set_chain function plays a crucial role in preparing the SpecificModel object for processing chat interactions seamlessly within the defined model context.

**Note**:
- The set_chain function relies on the create_runnable_chain function to create a functional chat message processing chain.
- Ensure valid prompts and a retriever object are provided to set up the chat processing chain effectively.
- Understanding the interaction between set_chain and create_runnable_chain is essential for comprehending the flow of chat message processing within the SpecificModel class.
***
### FunctionDef load_docs(self)
**load_docs**: The function of load_docs is to load documents from a specified directory using a DirectoryLoader, gather all the loaded documents, and assign them to the 'docs' attribute of the object.

**parameters**:
- None

**Code Description**: 
The load_docs function initializes an empty list named 'all_docs' to store the loaded documents. It then normalizes the path to the directory containing the documents and iterates through each subdirectory using os.walk. Within each subdirectory, it creates a DirectoryLoader object to load Markdown files ('.md') with the help of UnstructuredMarkdownLoader. The loaded documents are then added to the 'all_docs' list. Finally, the function assigns the aggregated documents to the 'docs' attribute of the object.

The load_docs function plays a crucial role in the SpecificModel class by enabling the loading of documents from a specified directory, which is essential for subsequent processing steps such as vector store configuration, retriever creation, and chat message processing chain establishment.

**Note**:
- Ensure that the 'path_marksdown' attribute of the object points to a valid directory containing Markdown files before calling the load_docs function.
- Understand that the successful execution of load_docs is a prerequisite for the proper functioning of other components within the SpecificModel class, such as retriever creation and chat message processing.
***
### FunctionDef get_docs(self)
**get_docs**: The function of get_docs is to return the value of the "docs" attribute stored in the object.

**parameters**: 
This Function does not take any parameters.

**Code Description**: 
The get_docs Function is a simple method that retrieves and returns the value of the "docs" attribute from the object it is called on.

**Note**: 
Developers using this Function should ensure that the "docs" attribute is properly set before calling get_docs to avoid any potential errors related to the attribute not being initialized.

**Output Example**: 
If the "docs" attribute in the object is set to "Sample documentation", calling get_docs will return the string "Sample documentation".
***
