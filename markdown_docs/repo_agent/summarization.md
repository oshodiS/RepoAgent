## ClassDef Summarizator
**Summarizator**: The function of Summarizator is to provide methods for summarizing a set of documents and generating a consolidated summary of their contents.

**attributes**:
- path: The path to the directory containing the documents.
- llm: An instance of the ChatOpenAI class for language modeling.
- docs: A list to store the documents.
- map_reduce_chain: A chain of operations for mapping and reducing the documents.

**Code Description**:
The Summarizator class initializes with a path to the document directory and a model name. It contains methods to split documents into chunks, read markdown files, and generate a consolidated summary of the documents.

The `get_map_reduce_chain` method sets up a chain of operations for mapping and reducing the documents using language models. It defines templates for mapping and reducing the documents, creates LLMChain instances, and configures the map-reduce chain for processing the documents.

The `split_documents` method splits a document into chunks based on specified headers and text size parameters.

The `read_md_files` method reads markdown files from a specified root path and returns a list of documents.

The `get_first_summarization` method reads markdown files from the specified path, splits them into chunks, sets up the map-reduce chain, and generates a consolidated summary of the documents.

The Summarizator class is called in the Runner class of the project to summarize markdown documents. The Runner class initializes various components including the Summarizator instance with the markdown folder path and model name for chat completion.

**Note**:
- Ensure the path provided to the Summarizator class points to a directory containing markdown files.
- The Summarizator class relies on external libraries and classes such as ChatOpenAI, LLMChain, and MarkdownHeaderTextSplitter for its operations.

**Output Example**:
A consolidated summary of the documents based on the mapping and reducing operations performed by the Summarizator class.
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
**get_map_reduce_chain**: The function of get_map_reduce_chain is to set up a chain of processes for mapping and reducing documents using LLMChain.

**parameters**:
- None

**Code Description**: 
The get_map_reduce_chain function initializes a map chain and a reduce chain using LLMChain with specific templates for mapping and reducing documents. It then creates chains for combining and reducing documents iteratively. Finally, it constructs a MapReduceDocumentsChain that combines the map and reduce chains to process a list of documents.

In the calling object get_first_summarization, after splitting the input documents, the get_map_reduce_chain function is invoked to generate a summary by running the map_reduce_chain on the split documents.

**Note**: 
- This function is crucial for setting up the document summarization process in the project.
- The map and reduce templates provide guidelines for creating descriptions and summaries.

**Output Example**: 
"The final consolidated summary captures the main points and key details from each document. The output_text contains the summarized content."
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
Ensure that the `doc` parameter is a valid document object.
Make sure to adjust the `chunk_size` and `chunk_overlap` parameters according to the desired splitting configuration.

**Output Example**:
```python
[
    Chunk 1: "Text chunk 1...",
    Chunk 2: "Text chunk 2...",
    ...
]
```
***
### FunctionDef read_md_files(slef, root_path)
**read_md_files**: The function of read_md_files is to read all Markdown files (.md) from a specified root path and return a list of documents.

**parameters**:
- root_path: The root path from which to start searching for Markdown files.

**Code Description**:
The `read_md_files` function iterates through all subdirectories in the specified `root_path` using `os.walk`. For each subdirectory, it creates a `DirectoryLoader` object to load all Markdown files (with the extension .md) using the `UnstructuredMarkdownLoader` class. The function then appends the loaded documents to the `all_docs` list. Finally, it returns the list of all loaded documents.

In the project, this function is called by the `get_first_summarization` method in the `Summarizator` class. The `get_first_summarization` method first prints the path, then calls `read_md_files` to load Markdown files. It processes the loaded documents by splitting them and assigning metadata. After preparing the data, it invokes a map-reduce chain and generates a summary based on the processed documents.

**Note**:
- Ensure that the `root_path` parameter is a valid directory path.
- Make sure that the `UnstructuredMarkdownLoader` class is correctly implemented to load Markdown files.

**Output Example**:
```python
[
    {
        'title': 'Document 1',
        'content': 'This is the content of document 1.',
        'metadata': {'author': 'Alice'}
    },
    {
        'title': 'Document 2',
        'content': 'This is the content of document 2.',
        'metadata': {'author': 'Bob'}
    },
    ...
]
```
***
### FunctionDef get_first_summarization(self)
**get_first_summarization**: The function of get_first_summarization is to generate a summary of the documents based on a map-reduce chain.

**parameters**:
- None

**Code Description**:
The `get_first_summarization` function is a crucial part of the document summarization process in the project. It starts by printing the path and then proceeds to read Markdown files using the `read_md_files` function. After reading the files, it splits the documents into smaller chunks using the `split_documents` function. The split documents are then processed using a map-reduce chain generated by the `get_map_reduce_chain` function. Finally, the function invokes the map-reduce chain on the split documents to generate a summary.

The `get_first_summarization` function first checks if there are any documents to summarize. If there are, it initializes an empty list called `all_splits` to store the split documents. It then iterates over each document and splits it into smaller chunks using the `split_documents` function. For each split document, it assigns a filename to the `metadata` attribute and adds it to the `all_splits` list. After splitting all the documents, it assigns the `all_splits` list to the `self.all_splits` attribute.

Next, the function calls the `get_map_reduce_chain` function to set up a map-reduce chain for processing the split documents. The `get_map_reduce_chain` function initializes a map chain and a reduce chain using LLMChain with specific templates for mapping and reducing documents. It then creates chains for combining and reducing documents iteratively. Finally, it constructs a MapReduceDocumentsChain that combines the map and reduce chains to process a list of documents. The resulting map-reduce chain is assigned to the `self.map_reduce_chain` attribute.

Finally, the function invokes the map-reduce chain on the split documents by calling the `invoke` method of the map-reduce chain. It retrieves the summarized output text from the map-reduce chain and assigns it to the `summary` variable. The `summary` variable is then returned as the output of the `get_first_summarization` function.

**Note**:
- The `get_map_reduce_chain` function is called within the `get_first_summarization` function to set up the map-reduce chain for processing the split documents.
- The `split_documents` function is called within the `get_first_summarization` function to split the input documents into smaller chunks.
- The `read_md_files` function is called within the `get_first_summarization` function to read Markdown files and return a list of documents.
- The `get_first_summarization` function is called by the `first_generate` and `run` methods in the `Runner` class.

**Output Example**:
"The final consolidated summary captures the main points and key details from each document. The output_text contains the summarized content."
***
