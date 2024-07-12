## FunctionDef split_documents(doc, chunk_size, chunk_overlap)
**split_documents**: The function of split_documents is to split a document into chunks of text.

**parameters**:
- doc: The document to be split into chunks.
- chunk_size: The size of each chunk (default value is 250).
- chunk_overlap: The number of characters to overlap between chunks (default value is 30).

**Code Description**:
The split_documents function takes a document as input and splits it into chunks of text based on specified parameters. It first defines headers to split on, then uses MarkdownHeaderTextSplitter and RecursiveCharacterTextSplitter to split the document into chunks. The function returns the splits.

In the project, split_documents is called by get_chunk_with_source in utilities.py to split a list of documents into chunks and assign a source metadata to each chunk. It is also called by get_first_summarization in parallel_summarization.py to split documents for parallel summarization.

**Note**:
- Ensure the input document is in a suitable format for splitting.
- Adjust the chunk_size and chunk_overlap parameters based on the desired chunk sizes and overlap.
- Understand the structure of the input document to determine the effectiveness of the splitting process.

**Output Example**:
```python
[
    Chunk 1,
    Chunk 2,
    ...
]
```
## FunctionDef get_chunk_with_source(docs, chunk_size, chunk_overlap)
**get_chunk_with_source**: The function of get_chunk_with_source is to split a list of documents into chunks and assign a source metadata to each chunk.

**parameters**:
- docs: The list of documents to be split into chunks.
- chunk_size: The size of each chunk (default value is 250).
- chunk_overlap: The number of characters to overlap between chunks (default value is 30).

**Code Description**:
The get_chunk_with_source function iterates over the input list of documents, splits each document into chunks using the split_documents function, and assigns a source metadata to each chunk based on the document's filename. The function then returns a list containing all the splits.

The split_documents function is utilized to split the documents into chunks based on specified parameters such as chunk size and overlap. This function is crucial for breaking down the documents effectively for further processing. Additionally, get_chunk_with_source is called by other functions in the project, such as set_vectorstore and get_chunk_docs in the Model class, to facilitate the chunking process for various purposes.

**Note**:
- Ensure the input documents are structured appropriately for splitting.
- Adjust the chunk_size and chunk_overlap parameters according to the desired chunk sizes and overlap for optimal results.
- Understanding the structure of the input documents is essential to ensure accurate chunking.

**Output Example**:
```python
[
    Chunk 1,
    Chunk 2,
    ...
]
```
## FunctionDef filter_docs(docs)
**filter_docs**: The function of filter_docs is to filter a list of documents based on the presence of "summary.md" in the metadata source.

**parameters**:
- docs: A list of documents to be filtered.

**Code Description**:
The filter_docs function iterates through the input list of documents and returns a new list containing only those documents where the metadata source includes the string "summary.md".

**Note**:
It is important to ensure that the input documents have a 'metadata' attribute with a 'source' key to avoid potential errors.

**Output Example**:
If the input list of documents is:
```python
[
    {"name": "Document1", "metadata": {"source": "summary.md"}},
    {"name": "Document2", "metadata": {"source": "content.md"}},
    {"name": "Document3", "metadata": {"source": "summary.md"}}
]
```

The output of filter_docs(docs) would be:
```python
[
    {"name": "Document1", "metadata": {"source": "summary.md"}},
    {"name": "Document3", "metadata": {"source": "summary.md"}}
]
```
## FunctionDef get_json_from_path(path)
**get_json_from_path**: The function of get_json_from_path is to load and return a JSON file from the specified path.

**parameters**:
- path: A string representing the file path of the JSON file to be loaded.

**Code Description**:
The get_json_from_path function opens the file specified by the path parameter in read mode with UTF-8 encoding. It then uses the json.load() method to load the JSON data from the file and returns it.

In the project, this function is called in the __init__ method of the Model class in the model.py file. The path_hierarchy parameter is passed to get_json_from_path to load a JSON file containing hierarchy information for the model.

**Note**:
It is important to ensure that the path parameter provided to the function is a valid path to a JSON file.

**Output Example**:
```json
{
    "key": "value"
}
```
## FunctionDef get_qa_system_prompt
**get_qa_system_prompt**: The function of get_qa_system_prompt is to retrieve a prompt for question-answering tasks related to code documentation.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_qa_system_prompt function returns a specific prompt for question-answering tasks regarding code documentation. The prompt includes instructions on how to use the retrieved context to answer questions related to the code documentation file. This function is designed to assist in generating relevant responses for code-related queries.

In the calling situation, the get_qa_system_prompt function is invoked within the set_chain method of the SpecificModel class. It retrieves the QA system prompt and incorporates it into the creation of prompt templates for the runnable chain. By using the prompt generated by get_qa_system_prompt, along with other prompts, the chain is set up to facilitate question-answering tasks within the context of the specific model.

**Note**: Developers can utilize the get_qa_system_prompt function to obtain a standardized prompt for handling question-answering tasks related to code documentation. The function's output can be further customized or combined with other prompts as needed for specific use cases.

**Output Example**: 
"You are an assistant for question-answering tasks regarding code documentation file. Use the following pieces of retrieved context to answer the question. It's also specified the name of the file that contains the functions. If you don't know the answer, say that you don't know. Use three sentences maximum and keep the answer concise.
{context}"
## FunctionDef get_contextualize_q_system_prompt
**get_contextualize_q_system_prompt**: The function of get_contextualize_q_system_prompt is to generate a reformulated standalone question based on the latest user question, which may reference context in the chat history.

**parameters**: 
- This Function does not take any parameters.

**Code Description**: 
The get_contextualize_q_system_prompt function returns a reformulated question that can be understood without the context of the chat history. It ensures that the question is standalone and does not include requests for additional information or clarification.

This function is crucial in the chatbot system as it helps in processing user questions effectively by providing a clear and concise standalone question. It is utilized to enhance the conversational flow and improve the user experience by ensuring that questions are presented in a coherent manner.

**Note**: 
Developers can use this function to preprocess user questions before further analysis or response generation in the chatbot system. It is essential to integrate this function correctly within the system to maintain the conversational context and provide accurate responses.

**Output Example**: 
"Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is. Do NOT add requests for additional information or clarification if not in the original question. keep it as a question"
## FunctionDef get_dont_contextualize_system_prompt
**get_dont_contextualize_system_prompt**: The function of get_dont_contextualize_system_prompt is to return a specific system prompt for chat interactions.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_dont_contextualize_system_prompt function returns a system prompt that instructs the system to repeat the question as it is without adding requests for additional information or answering the question.

In the project, this function is called in two different contexts:
1. In the GeneralModel class, the set_chain method uses this function to retrieve the system prompt and create a runnable chain for the general model.
2. In the SpecificModel class, the set_chain method also utilizes this function to get the system prompt along with another prompt for creating a runnable chain for the specific model.

**Note**: Developers can use this function to obtain a predefined system prompt for chat interactions without contextualizing the question.

**Output Example**: 
"Repeat the question as it is. Do NOT add requests for additional information or clarification if not in the original question. Do NOT answer the question."
## FunctionDef get_readme_path(root_path)
**get_readme_path**: The function of get_readme_path is to search for the README.md file within the root of a repository and return its path if found.

**parameters**:
- root_path: The root path of the repository to search for the README.md file.

**Code Description**:
The get_readme_path function starts by compiling a regular expression pattern to match README.md or README.txt files case-insensitively. It then normalizes and obtains the absolute path of the root directory. The function iterates through all files in the directory and its subdirectories using os.walk. If a file matches the pattern, the function returns the full path to that file. If no README file is found, it returns None.

This function is utilized in the project in the following way:
- In the GeneralModel class within general_model.py, the load_docs method calls get_readme_path to determine the path of the README.md file in the repository root. Depending on the existence of the README file, different loaders are used to load the documentation.
- In the refresh_summary function in main.py, get_readme_path is used to check if a README file exists in the target repository. If not found, a summarization process is initiated and a summary file is generated based on the content.
- In the first_generate method of the Runner class in runner.py, get_readme_path is employed to verify the presence of a README file in the target repository. If the file is missing, a summarization process is triggered to generate a summary file.

**Note**: 
- This function is essential for locating the README file in a repository, which is often used for documentation purposes.
- It is crucial to ensure the correct root path is provided to the function for accurate results.

**Output Example**:
If the README.md file is found in the repository root, the function will return something like: "C:/project/repo_agent/README.md". If no README file is found, the function will return None.
## FunctionDef load_docs(path_marksdown)
**load_docs**: The function of load_docs is to load markdown documents from a specified path.

**parameters**:
- path_marksdown: A string representing the path to the markdown documents.

**Code Description**:
The `load_docs` function takes a path to markdown documents as input. It normalizes the path and iterates through each subdirectory to load markdown files. For each subdirectory, it instantiates a `DirectoryLoader` with specific parameters and loads the markdown documents using a `UnstructuredMarkdownLoader`. Any exceptions that occur during the loading process are caught and printed. Finally, all loaded documents are collected and returned as a list.

In the project, this function is called by different objects such as `SpecificModel` and `ParallelSummarizator` to load markdown documents from specified paths for further processing. For example, in `SpecificModel`, the loaded documents are used to set up a vector store and metadata field information for a retriever. In `ParallelSummarizator`, the loaded documents are split into chunks and processed to generate a summary.

**Note**:
- Ensure the path provided is valid and contains markdown documents.
- Handle any exceptions that may occur during the loading process.

**Output Example**:
```python
[
    <Document1>,
    <Document2>,
    ...
]
```
