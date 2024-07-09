## FunctionDef split_documents(doc, chunk_size, chunk_overlap)
**split_documents**: The function of split_documents is to split a document into chunks of text.

**parameters**:
- doc: The input document to be split into chunks.
- chunk_size: The size of each chunk (default value is 250).
- chunk_overlap: The number of characters to overlap between consecutive chunks (default value is 30).

**Code Description**:
The split_documents function takes a document as input and splits it into chunks of text based on specified parameters. It first defines headers to split on, then uses a MarkdownHeaderTextSplitter to split the document based on headers. Next, it utilizes a RecursiveCharacterTextSplitter to further split the text into chunks of the specified size with the defined overlap. Finally, it returns the splits.

In the project, the split_documents function is called by the get_chunk_with_source function. The get_chunk_with_source function iterates over a list of documents, calls split_documents on each document, assigns a source metadata to each split based on the document's filename, and aggregates all the splits into a single list before returning it.

**Note**:
- Ensure the input document is in a format that can be split based on headers and characters.
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
**get_contextualize_q_system_prompt**: The function of get_contextualize_q_system_prompt is to formulate a standalone question from a given chat history and the latest user question, ensuring it can be understood without the context of the chat history. 

**parameters**: This Function does not take any parameters.

**Code Description**: The get_contextualize_q_system_prompt function returns a reformulated question based on the latest user question and chat history provided. It ensures that the question can stand alone without the need for context from the chat history.

This function is utilized in different parts of the project:
1. In the ClassificationModel class in classification_model2.py, the function is used to set the contextualize_q_prompt by incorporating the system prompt generated by get_contextualize_q_system_prompt.
2. In the GeneralModel class in general_model.py, the function is called to set up the chain by obtaining the contextualize_q_system_prompt and creating a runnable chain using the provided template and retriever.
3. In the SpecificModel class in specific_model.py, the function is used to set up the chain along with another prompt, qa_system_prompt, by creating prompt templates and setting up the runnable chain.

**Note**: This function is designed to assist in generating standalone questions from user input and chat history, ensuring clarity and context independence.

**Output Example**: 
"Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."
