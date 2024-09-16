## ClassDef Summarizator
**Summarizator**: The function of Summarizator is to provide a mechanism for summarizing a set of documents by mapping and reducing their contents into a consolidated summary.

**attributes**:
- path: The path to the directory containing the documents.
- llm: An instance of the ChatOpenAI class used for language modeling.
- docs: A list to store the loaded documents.
- map_reduce_chain: A chain of operations for mapping and reducing document contents.

**Code Description**:
The Summarizator class initializes with a path to the document directory and a model name. It contains methods to split documents into chunks, retrieve the first summarization, and read markdown files from the specified path. The get_map_reduce_chain method sets up a chain of operations for mapping and reducing document contents. The split_documents method splits a document into chunks based on headers. The get_first_summarization method reads markdown files, splits them into chunks, and invokes the map_reduce_chain to generate a summary.

**Note**:
- Ensure the path provided leads to a directory containing markdown files for summarization.
- The summarization process involves mapping and reducing document contents to create a concise summary.

**Output Example**:
"A concise summary capturing the main points and key details from the provided documents."
### FunctionDef __init__(self, path, model_name)
**__init__**: The function of __init__ is to initialize the object with the provided path and model name.

**parameters**:
- path: A string representing the path to the model.
- model_name: A string specifying the name of the model.

**Code Description**:
In this function, the provided path and model name are assigned to the object's attributes. Additionally, a ChatOpenAI instance is created with a temperature of 0.1 and the specified model name. The attributes "docs" and "map_reduce_chain" are initialized to None.

**Note**:
Ensure that the path and model name are correctly provided when initializing an instance of this object.
***
### FunctionDef get_map_reduce_chain(self)
**get_map_reduce_chain**: The function of get_map_reduce_chain is to create a chain of processes for mapping and reducing documents using LLMChain.

**parameters**:
- No parameters are passed explicitly to the function.

**Code Description**:
The get_map_reduce_chain function initializes two LLMChain instances, one for mapping and one for reducing documents. It then sets up a chain of processes to combine and reduce the mapped documents iteratively. The final MapReduceDocumentsChain is created with the map_chain, reduce_documents_chain, document_variable_name, and return_intermediate_steps parameters. Additionally, the function loads a summarize chain using the load_summarize_chain function with the llm and chain_type parameters.

In the calling object get_first_summarization, the function reads markdown files, splits them into smaller parts, and invokes the get_map_reduce_chain function to process the splits using the map_reduce_chain. The output text from the map_reduce_chain is then returned as the summary.

**Note**:
- The get_map_reduce_chain function is essential for setting up the mapping and reducing processes for document summarization.
- Ensure that the necessary LLM model is initialized before calling this function to avoid errors.

**Output Example**:
"The final consolidated summary captures the main points and key details from each document, providing a concise overview of the contents."
***
### FunctionDef split_documents(self, doc, chunk_size, chunk_overlap)
**split_documents**: The function of split_documents is to split a document into chunks of text.

**parameters**:
- doc: The document to be split into chunks.
- chunk_size: The size of each chunk of text.
- chunk_overlap: The overlap between chunks.

**Code Description**:
The `split_documents` function takes a document, `doc`, and splits it into chunks of text based on specified parameters. It first defines headers to split on, then uses a MarkdownHeaderTextSplitter to split the document based on headers. Next, it utilizes a RecursiveCharacterTextSplitter to further split the text into chunks based on the chunk size and overlap. Finally, it returns the splits.

In the project, this function is called within the `get_first_summarization` method of the `Summarizator` class. The `get_first_summarization` method reads Markdown files, splits them using `split_documents`, processes the splits, and generates a summary using a map-reduce chain.

**Note**:
- Ensure the `doc` parameter is a valid document object.
- Adjust the `chunk_size` and `chunk_overlap` parameters based on the desired chunking configuration.

**Output Example**:
```python
[
    Chunk 1: "Text chunk 1...",
    Chunk 2: "Text chunk 2...",
    ...
]
```
***
### FunctionDef get_first_summarization(self)
**get_first_summarization**: The function of get_first_summarization is to read Markdown files, split them into smaller parts, process the splits using a map-reduce chain, and return the generated summary.

**parameters**:
- No explicit parameters are passed to this function.

**Code Description**: 
The get_first_summarization function first reads Markdown files using the read_md_files function. It then splits the documents into smaller parts using the split_documents function. After splitting, it invokes the get_map_reduce_chain function to process the splits using a map-reduce chain. Finally, the function returns the output text from the map-reduce chain as the summary.

In the context of the project, get_first_summarization serves as a crucial function in the document summarization process. By leveraging the read_md_files, split_documents, and get_map_reduce_chain functions, it efficiently processes and summarizes the content of Markdown files.

**Note**:
- Ensure that the necessary Markdown files are available in the specified path for proper execution.
- It is essential to have the get_map_reduce_chain function properly set up before calling get_first_summarization to ensure accurate summarization.

**Output Example**:
"The final consolidated summary captures the main points and key details from each document, providing a concise overview of the contents."
***
### FunctionDef read_md_files(root_path)
**read_md_files**: The function of read_md_files is to read all Markdown files (.md) within a specified root path and return a list of documents.

**parameters**:
- root_path: The root directory path where the function will start searching for Markdown files.

**Code Description**:
The read_md_files function first normalizes and converts the root_path to an absolute path. It then iterates through all subdirectories under the root_path using os.walk. For each subdirectory, it creates a DirectoryLoader object to load all Markdown files (with the .md extension) using UnstructuredMarkdownLoader. The function collects all loaded documents into a list and returns this list of documents.

In the project, the read_md_files function is called within the get_first_summarization method of the Summarizator class. In this context, read_md_files is used to load Markdown files from a specified path, which are later split and processed to generate a summary.

**Note**:
- Ensure the root_path provided is a valid directory path.
- Make sure the Markdown files have the .md extension for proper loading.

**Output Example**:
[doc1, doc2, doc3, ...]
***
