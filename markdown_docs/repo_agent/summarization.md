## ClassDef Summarizator
**Summarizator**: The function of Summarizator is to provide a mechanism for summarizing a set of documents by mapping and reducing their contents.

**attributes**:
- path: The path to the directory containing the documents.
- llm: An instance of the ChatOpenAI class used for language modeling.
- docs: A list to store the loaded documents.
- map_reduce_chain: A chain of operations for mapping and reducing document contents.

**Code Description**:
The Summarizator class initializes with a path to the document directory and a model name. It utilizes a ChatOpenAI instance for language modeling. The class provides methods to split documents into chunks, read Markdown files, and generate a summary by mapping and reducing document contents.

The get_map_reduce_chain method sets up a chain of operations for mapping and reducing document contents. It defines templates for mapping and reducing prompts, creates LLMChain instances, and configures chains for combining and reducing documents. The method ultimately sets the map_reduce_chain attribute to handle the summarization process.

The split_documents method splits a document into chunks based on specified parameters such as chunk size and overlap. It utilizes MarkdownHeaderTextSplitter and RecursiveCharacterTextSplitter to perform the splitting operation.

The get_first_summarization method reads Markdown files from the specified directory, splits the documents into chunks, sets up the map_reduce_chain, and invokes the chain to generate a summary of the document contents.

The read_md_files method reads Markdown files from the specified root path using a DirectoryLoader and returns a list of loaded documents.

**Note**:
- Ensure the path provided to the Summarizator instance points to a valid directory containing Markdown files for summarization.
- The summarization process involves mapping and reducing document contents to generate a consolidated summary.

**Output Example**:
"A concise summary of the overall contents based on the provided documents."
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
**get_map_reduce_chain**: The function of get_map_reduce_chain is to set up a map-reduce chain for processing a list of documents.

**parameters**:
- None

**Code Description**:
The `get_map_reduce_chain` function initializes a map chain and a reduce chain using LLMChain with specific templates for mapping and reducing documents. It then creates chains for combining and reducing documents iteratively. Subsequently, it constructs a MapReduceDocumentsChain that combines the map and reduce chains to process a list of documents. The resulting map-reduce chain is assigned to the `self.map_reduce_chain` attribute.

In the project, the `get_map_reduce_chain` function is called within the `get_first_summarization` function to establish the map-reduce chain for processing split documents. The `get_first_summarization` function is invoked by the `first_generate` and `run` methods in the `Runner` class.

**Note**:
- The `get_map_reduce_chain` function plays a crucial role in setting up the map-reduce chain for document processing.
- It is an essential component in the document summarization process within the project.
- The function is part of a chain of functions that work together to generate a consolidated summary of input documents.

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
### FunctionDef get_first_summarization(self)
**get_first_summarization**: The function of get_first_summarization is to process a list of documents by splitting them into chunks, setting up a map-reduce chain, and generating a consolidated summary.

**parameters**:
- None

**Code Description**: 
The `get_first_summarization` function reads Markdown files, splits them into chunks, sets up a map-reduce chain using the `get_map_reduce_chain` function, and generates a summary by invoking the map-reduce chain. It iterates through the documents, splits them into manageable chunks, assigns metadata to each split, and then processes them through the map-reduce chain to produce a final summary. This function is a key component in the document summarization process within the project.

**Note**:
- Ensure that the documents are in Markdown format for proper processing.
- The function relies on the `split_documents` and `get_map_reduce_chain` functions to split documents and set up the map-reduce chain, respectively.

**Output Example**:
"The final consolidated summary captures the main points and key details from each document. The output_text contains the summarized content."
***
### FunctionDef read_md_files(root_path)
**read_md_files**: The function of read_md_files is to read Markdown files from a specified root path and return a list of all the documents found.

**parameters**:
- root_path: The root path from which Markdown files will be read.

**Code Description**:
The `read_md_files` function begins by normalizing and converting the `root_path` to an absolute path. It then iterates through all subdirectories in the `root_path` using `os.walk`. For each subdirectory, it creates a `DirectoryLoader` instance to load Markdown files with the specified glob pattern "./*.md" and using the `UnstructuredMarkdownLoader` loader class. The function then loads the documents using the loader and appends them to the `all_docs` list. Finally, it returns the list of all loaded documents.

The `read_md_files` function is called within the `get_first_summarization` function in the `Summarizator` class to read Markdown files for further processing in the document summarization pipeline.

**Note**:
- Ensure that the `root_path` parameter is a valid path to the directory containing Markdown files.
- The function relies on the `DirectoryLoader` class and the `UnstructuredMarkdownLoader` loader class to load Markdown files.

**Output Example**:
An example output of the `read_md_files` function could be a list of Markdown documents like:
["document1.md", "document2.md", "document3.md"]
***