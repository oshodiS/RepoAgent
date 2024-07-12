## ClassDef ChromaManager
**ChromaManager**: The function of ChromaManager is to manage the creation and storage of data collections in ChromaDB.

**attributes**:
- api_key: The API key used for authentication.
- api_base: The base URL for API requests.
- chroma_collection: The collection of data stored in ChromaDB.
- is_new_collection: A boolean flag indicating whether the collection is new or existing.

**Code Description**:
The `ChromaManager` class initializes with an API key and base URL. It manages the creation and storage of data collections in ChromaDB. Upon initialization, it sets the `chroma_collection` attribute to `None` and `is_new_collection` to `False`, then calls the `init_chroma_collection` method.

The `init_chroma_collection` method initializes a ChromaDB client, checks for existing collections, and either loads an existing collection named "test" or creates a new one if it does not exist. It handles exceptions for UniqueConstraintError when attempting to create a collection that already exists.

The `create_vector_store` method processes Markdown content and stores it in the Chroma collection. It checks if the collection is new and adds the content accordingly. If the collection is not new, it logs a debug message.

The `ChromaManager` class plays a crucial role in managing data collections in ChromaDB, ensuring efficient storage and retrieval of data for further processing.

**Note**:
Developers using the `ChromaManager` class should ensure they have the necessary API key and base URL for ChromaDB operations. They should also handle exceptions appropriately when working with data collections to maintain data integrity.
### FunctionDef __init__(self, api_key, api_base)
**__init__**: The function of __init__ is to initialize the ChromaManager object with the provided API key, API base, and default values for the Chroma collection and new collection flag.

**parameters**:
- api_key: The API key used for authentication.
- api_base: The base URL for API requests.

**Code Description**:
The __init__ function initializes the ChromaManager object by setting the API key and API base provided as parameters. It also initializes the chroma_collection attribute to None and the is_new_collection attribute to False. Additionally, it calls the init_chroma_collection method to manage the initialization of the Chroma collection based on the existence of the "test" collection.

The init_chroma_collection method creates a PersistentClient object for the Chroma database, checks for the existence of the "test" collection, and either loads the existing collection or creates a new one. The function sets the is_new_collection flag based on whether a new collection was created during the process.

This function establishes the initial state of the ChromaManager object by setting up the necessary attributes and initializing the Chroma collection based on the provided API key and API base. It ensures that the ChromaManager object is ready to interact with the Chroma database for further operations.

**Note**:
- The __init__ function is crucial for setting up the ChromaManager object with the required parameters and initializing the Chroma collection.
- It relies on the init_chroma_collection method to handle the creation or loading of the Chroma collection based on the existence of the "test" collection.
***
### FunctionDef init_chroma_collection(self)
**init_chroma_collection**: The function of init_chroma_collection is to initialize a Chroma collection by either loading an existing collection named "test" or creating a new one if it does not exist.

**parameters**:
- No external parameters are passed to this function.

**Code Description**:
The init_chroma_collection function first creates a PersistentClient object for the Chroma database with a specified path. It then retrieves a list of existing collections using the list_collections method of the chroma_client. If the collection named "test" is found in the existing collections, the function loads this collection using the get_collection method with specific embedding function parameters. If the "test" collection does not exist, a new collection is created using the create_collection method with the same embedding function parameters. In case of a UniqueConstraintError during the creation attempt, the function handles the error by loading the existing "test" collection. Finally, the function sets the is_new_collection flag accordingly.

This function is called during the initialization of the ChromaManager object in the __init__ method. Additionally, it is tested in the test_init_chroma_collection method of the TestChromaManager class to ensure the proper initialization of the Chroma collection.

**Note**:
- This function is responsible for managing the initialization of the Chroma collection, either by loading an existing collection or creating a new one.
- The function relies on the Chroma database client and specific embedding function parameters for collection operations.
***
### FunctionDef create_vector_store(self, md_contents, meta_data)
**create_vector_store**: The function of create_vector_store is to process Markdown content and store it in Chroma, ensuring that the length of ids matches the shorter of md_contents and meta_data.

**parameters**:
- self: The instance of the class.
- md_contents: A list of Markdown content.
- meta_data: A list of metadata associated with the Markdown content.

**Code Description**:
The create_vector_store function first checks if it is a new collection. If it is a new collection, it calculates the minimum length between md_contents and meta_data, generates ids based on this length, and then adds the documents and metadata to the Chroma collection. If it is not a new collection, it logs a debug message.

In the calling situation, the create_vector_store function is invoked in the main function of the 'main.py' file in the 'chat_with_repo' module. It is called after extracting data and before initializing the GradioInterface, indicating that it plays a crucial role in preparing the data for further processing and interaction with the GradioInterface.

In the test scenario, the create_vector_store function is tested in the 'test_create_vector_store' test case in the 'test_vectordb.py' file. The test verifies that the method correctly calls the embedding function with the provided Markdown content and adds the documents with their embeddings to the collection.

**Note**:
- Ensure that the lengths of md_contents and meta_data are compatible to avoid any mismatch issues.
- Understand the context in which the function is called to grasp its significance in the overall workflow of the project.
***
