## ClassDef SpecificModel
**SpecificModel**: The function of SpecificModel is to create a specific model instance tailored for the chat_langchain project.

**Attributes**:
- `path`: The path to the model.
- `path_hierarchy`: The path to the hierarchy file.
- `model_name`: The name of the model.
- `chunk_size`: The size of each data chunk.
- `chunk_overlap`: The overlap between data chunks.

**Code Description**:
The `SpecificModel` class extends the `Model` class and initializes the model with the provided path, path hierarchy, model name, chunk size, and chunk overlap. It loads documents, sets the vector store, defines metadata field information, creates a retriever, and sets up the chain for the model.

The `set_chain` method sets up the chain by creating prompt templates for history and QA systems.

The `get_docs` method returns the loaded documents.

**Note**: The `SpecificModel` class is designed to provide specific functionalities for the chat_langchain project and should be used within the project context.

**Output Example**:
```python
specific_model = SpecificModel(path="model_path", path_hierarchy="hierarchy_path", model_name="specific_model", chunk_size=1000, chunk_overlap=100)
docs = specific_model.get_docs()
```
### FunctionDef __init__(self, path, path_hierarchy, model_name, chunk_size, chunk_overlap)
**__init__**: The function of __init__ is to initialize the SpecificModel object with the provided parameters, load documents, set up a vector store, configure metadata field information, create a retriever object, and establish the chatbot system chain.

**parameters**:
- path: The path to the markdown documents.
- path_hierarchy: The hierarchy of the path.
- model_name: The name of the model.
- chunk_size: The size of each text chunk.
- chunk_overlap: The overlap between text chunks.

**Code Description**:
The __init__ method initializes the SpecificModel object by loading markdown documents from the specified path using the load_docs function. It then sets up the vector store by calling the set_vectorstore method with the provided chunk size, chunk overlap, and collection name. Subsequently, metadata field information is configured, and a retriever object is created using SelfQueryRetriever. Finally, the set_chain method is invoked to establish the chatbot system chain, incorporating question answering prompts, conversation history prompts, and the retriever object.

The set_vectorstore function is called within __init__ to prepare document chunks for vectorization, while the set_chain function is utilized to initialize the chatbot system. This method plays a crucial role in setting up the SpecificModel object for effective question answering and conversation management within the chatbot system.

**Note**:
- Ensure the path provided contains the necessary markdown documents.
- Set appropriate values for chunk_size and chunk_overlap to optimize text chunking.
- Understand the interdependency between set_vectorstore, set_chain, and other methods for seamless chatbot system initialization.
***
### FunctionDef set_chain(self)
**set_chain**: The function of set_chain is to initialize the chatbot system by creating prompt templates using utility functions and setting up a chain of operations incorporating question answering prompts, conversation history prompts, and a retriever object.

**parameters**:
- This function does not take any parameters.

**Code Description**:
The set_chain function first retrieves a system prompt for conversation history from the get_dont_contextualize_system_prompt utility function. It then obtains a question-answering prompt using the get_qa_system_prompt utility function. Subsequently, the function utilizes the create_runnable_chain method from the Model class to construct a chain of operations for the chatbot system. This chain includes the question answering prompt, conversation history prompt, and the retriever object. By creating prompt templates and setting up the operational flow, the set_chain function plays a vital role in establishing the foundation for effective question answering and conversation management within the chatbot system.

In the project, the set_chain function is called within the __init__ method of the SpecificModel class. This method is responsible for initializing various components of the SpecificModel, including loading documentation, setting vector stores, configuring metadata field information, creating a retriever object, and ultimately setting up the chatbot system by invoking the set_chain function. The integration of set_chain within the SpecificModel class showcases its significance in the overall setup and functionality of the chatbot system.

**Note**:
Developers utilizing the set_chain function should ensure that the utility functions for prompts are correctly configured to align with the chatbot's requirements. Understanding the role of set_chain in initializing the chatbot system is crucial for ensuring smooth operation and effective handling of user queries and conversation history.
***
### FunctionDef get_docs(self)
**get_docs**: The function of get_docs is to return the value of the "docs" attribute stored in the object.

**parameters**: 
This Function does not take any parameters.

**Code Description**: 
The get_docs function is a method of the SpecificModel class. When called, it retrieves and returns the value of the "docs" attribute that is stored within the object instance.

**Note**: 
Developers can use this function to access the documentation or any information stored in the "docs" attribute of the SpecificModel object.

**Output Example**: 
If the "docs" attribute contains the value "This is the documentation for the SpecificModel class", calling get_docs() will return "This is the documentation for the SpecificModel class".
***
