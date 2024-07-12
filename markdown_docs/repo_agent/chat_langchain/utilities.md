## FunctionDef split_documents(doc, chunk_size, chunk_overlap)
**split_documents**: The function of split_documents is to split a document into chunks of text.

**parameters**:
- doc: The input document to be split into chunks.
- chunk_size: The size of each chunk (default value is 250).
- chunk_overlap: The number of characters to overlap between consecutive chunks (default value is 30).

**Code Description**:
The split_documents function takes a document as input and splits it into chunks of text based on the specified chunk size and overlap. It first defines headers to split on, then utilizes MarkdownHeaderTextSplitter and RecursiveCharacterTextSplitter to split the document. The function returns the splits of the document.

This function is called by the get_chunk_with_source function in the utilities.py file. In the get_chunk_with_source function, split_documents is used to split a list of documents into chunks and assign a source metadata to each chunk based on the document's filename. The output of split_documents is further processed to aggregate all splits into a single list.

**Note**:
- Ensure the input document is in a format that can be split into chunks based on the specified parameters.
- Adjust the chunk_size and chunk_overlap parameters as needed to control the size and overlap of the text chunks.

**Output Example**:
```
[
    Chunk 1,
    Chunk 2,
    ...
]
```
## FunctionDef get_chunk_with_source(docs, chunk_size, chunk_overlap)
**get_chunk_with_source**: The function of get_chunk_with_source is to split a list of documents into chunks of text and assign a source metadata to each chunk based on the document's filename.

**parameters**:
- docs: A list of documents to be split into chunks.
- chunk_size: The size of each chunk (default value is 250).
- chunk_overlap: The number of characters to overlap between consecutive chunks (default value is 30).

**Code Description**:
The get_chunk_with_source function iterates over the input list of documents. For each document, it calls the split_documents function to split the document into chunks based on the specified chunk size and overlap. After splitting, it assigns a source metadata to each chunk using the document's filename. Finally, all the splits are aggregated into a single list and returned.

In the project, the get_chunk_with_source function is utilized by other functions in the model.py file. Specifically, it is called by the set_vectorstore and get_chunk_docs functions in the Model class. These functions use the output of get_chunk_with_source to create a vector store for the documents or return the split chunks, respectively.

**Note**:
- Ensure the input documents are in a format that can be split into chunks based on the specified parameters.
- Adjust the chunk_size and chunk_overlap parameters as needed to control the size and overlap of the text chunks.

**Output Example**:
```
[
    Chunk 1,
    Chunk 2,
    ...
]
```
## FunctionDef filter_docs(docs)
**filter_docs**: The function of filter_docs is to filter a list of documents based on the presence of "summary.md" in the metadata source field.

**parameters**:
- docs: A list of documents to be filtered.

**Code Description**:
The filter_docs function iterates through the input list of documents and selects only those documents where the string "summary.md" is found in the 'source' field of the document's metadata. It then returns a new list containing only the filtered documents.

**Note**:
It is important to ensure that the input documents have a 'metadata' field containing a 'source' key to avoid potential errors.

**Output Example**:
If the input list of documents is:
```python
[
    {'metadata': {'source': 'summary.md', 'type': 'article'}},
    {'metadata': {'source': 'intro.txt', 'type': 'tutorial'}},
    {'metadata': {'source': 'chapter1.md', 'type': 'guide'}},
    {'metadata': {'source': 'summary.md', 'type': 'article'}}
]
```

The output of filter_docs(docs) would be:
```python
[
    {'metadata': {'source': 'summary.md', 'type': 'article'}},
    {'metadata': {'source': 'summary.md', 'type': 'article'}}
]
```
## FunctionDef get_json_from_path(path)
**get_json_from_path**: The function of get_json_from_path is to load and return JSON data from a specified file path.

**parameters**:
- path: A string representing the file path from which JSON data will be loaded.

**Code Description**:
The get_json_from_path function opens the file specified by the path parameter in read mode with UTF-8 encoding. It then loads the JSON data from the file and returns it.

In the project, this function is called within the __init__ method of the Model class in the model.py file. The path_hierarchy parameter is passed to get_json_from_path to load JSON data from the specified path_hierarchy file.

**Note**:
It is important to ensure that the file path provided to the get_json_from_path function is correct and the file exists to avoid any file handling errors.

**Output Example**:
{
    "key": "value",
    "key2": "value2"
}
## FunctionDef get_qa_system_prompt
**get_qa_system_prompt**: The function of get_qa_system_prompt is to retrieve a prompt template for question-answering tasks related to code documentation files.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_qa_system_prompt function returns a specific prompt template for assisting in answering questions related to code documentation files. The prompt includes instructions on how to utilize the retrieved context to provide answers effectively within a limited number of sentences.

In the project, this function is called within the set_chain method of the SpecificModel class. In this context, the returned prompt template is used to create a runnable chain for question-answering tasks, along with other templates obtained from different functions.

**Note**: Developers can use the prompt template returned by this function to guide the process of answering questions regarding code documentation files efficiently.

**Output Example**: 
"You are an assistant for question-answering tasks regarding code documentation file. Use the following pieces of retrieved context to answer the question. It's also specified the name of the file that contains the functions. If you don't know the answer, say that you don't know. Use three sentences maximum and keep the answer concise.
{context}"
## FunctionDef get_contextualize_q_system_prompt
**get_contextualize_q_system_prompt**: The function of get_contextualize_q_system_prompt is to formulate a standalone question from a chat history and the latest user question, ensuring clarity and independence from the context of the chat history.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_contextualize_q_system_prompt function returns a reformulated user question that can be understood without the context of the chat history. It ensures that the question remains a question, reframing it only if necessary to maintain clarity and independence from the chat history.

This function is utilized within the __set_contextualize_prompt method in the ClassificationModel class to set up a contextualized question prompt. The __set_contextualize_prompt method combines the system prompt generated by get_contextualize_q_system_prompt with the chat history and the latest user input to create a ChatPromptTemplate. This template enhances the classification model's ability to interpret user queries accurately within the chat context.

**Note**: The get_contextualize_q_system_prompt function is essential for preparing clear and context-independent questions, contributing to the effectiveness of the contextualized prompts used in the classification model.

**Output Example**: 
"Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is. Do NOT add requests for additional information or clarification if not in the original question. keep it as a question"
## FunctionDef get_dont_contextualize_system_prompt
**get_dont_contextualize_system_prompt**: The function of get_dont_contextualize_system_prompt is to retrieve a system prompt instructing to repeat the original question without adding additional information or answering it.

**parameters**: 
- This function does not take any parameters.

**Code Description**: 
The get_dont_contextualize_system_prompt function returns a system prompt advising to repeat the question as is without adding any extra information or answering it. This prompt is designed to maintain the original context of the question without alterations.

This function is called within the set_chain methods of both GeneralModel and SpecificModel classes in the project. In GeneralModel, it is used to initialize a chat processing chain by providing a prompt for the chain creation process. In SpecificModel, it is utilized to set up a retrieval chain by obtaining a specific system prompt.

**Note**: 
- The returned prompt is crucial for maintaining the original context of questions within the chat processing chain.
- Ensure the prompt is appropriately used within the context of initializing chat processing chains.

**Output Example**: 
"Repeat the question as it is. Do NOT add requests for additional information or clarification if not in the original question. Do NOT answer the question."
## FunctionDef get_readme_path(root_path)
**get_readme_path**: The function of get_readme_path is to retrieve the path of the README.md file in the specified repository root directory.
**parameters**:
- root_path: The root directory path of the repository.

**Code Description**:
The get_readme_path function starts by compiling a regular expression pattern to match README.md or README.txt files in a case-insensitive manner. It then normalizes and obtains the absolute path of the root directory. By traversing the directory structure using os.walk, the function searches for files that match the specified pattern. If a matching file is found, the function returns the full path to that file. If no matching file is found, it returns None.

In the project context, the get_readme_path function is utilized by the load_docs method in the GeneralModel class to determine the path of the README.md file in the repository. This path is crucial for loading documents for further processing within the GeneralModel instance.

**Note**:
- It is essential to ensure that the README.md file follows the expected naming conventions for successful path retrieval.
- The root_path parameter should point to the root directory of the repository for accurate path determination.
- Proper initialization of the GeneralModel instance is necessary before invoking the load_docs method to ensure correct document loading.

**Output Example**:
If the README.md file is found in the specified repository root directory, the function may return a path like: "/path/to/repository/README.md".
## FunctionDef load_docs(path_marksdown)
**load_docs**: The function of load_docs is to load documents from a specified path, process each document, and return a list of all loaded documents.
**parameters**:
- path_marksdown: The path to the directory containing the documents in markdown format.

**Code Description**:
The load_docs function begins by normalizing the provided path and converting it to an absolute path. It then iterates through all subdirectories in the specified path, using a DirectoryLoader to load documents with the specified file extension ".md" and loader class UnstructuredMarkdownLoader. The function aggregates all loaded documents into a single list and returns this list.

The load_docs function is a crucial utility for retrieving and processing documents stored in markdown format within a specified directory. It facilitates the efficient loading of multiple documents for further analysis or manipulation within the application.

**Note**:
- Ensure that the path provided contains valid markdown documents for successful loading.
- Utilize the returned list of documents for subsequent processing or analysis within the application.

**Output Example**:
[doc1, doc2, doc3, ...]
