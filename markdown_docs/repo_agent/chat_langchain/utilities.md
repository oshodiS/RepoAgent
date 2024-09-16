## FunctionDef split_documents(doc, chunk_size, chunk_overlap)
**split_documents**: The function of split_documents is to split a document into chunks of text.

**parameters**:
- doc: The document to be split into chunks.
- chunk_size: The size of each chunk of text (default value is 250).
- chunk_overlap: The number of characters to overlap between chunks (default value is 30).

**Code Description**:
The split_documents function takes a document and splits it into chunks of text based on specified parameters. It first defines headers to split on, then uses a MarkdownHeaderTextSplitter to split the document based on headers. Next, it utilizes a RecursiveCharacterTextSplitter to further split the text into chunks based on the chunk_size and chunk_overlap parameters. Finally, it returns the splits.

This function is called by other functions in the project, such as get_chunk_with_source in utilities.py and get_first_summarization in ParallelSummarizator class in parallel_summarization.py. In get_chunk_with_source, split_documents is used to split each document in a list of documents and assign a source metadata to each split. In get_first_summarization, split_documents is used to split documents loaded from a path and prepare them for parallel summarization.

**Note**:
- Ensure the input document is in a format that can be split based on headers and characters.
- Adjust the chunk_size and chunk_overlap parameters according to the desired chunking behavior.

**Output Example**:
```python
[
    Chunk 1: "Text chunk 1...",
    Chunk 2: "Text chunk 2...",
    ...
]
```
## FunctionDef get_chunk_with_source(docs, chunk_size, chunk_overlap)
**get_chunk_with_source**: The function of get_chunk_with_source is to split a list of documents into chunks of text and assign a source metadata to each chunk based on the document's filename.

**parameters**:
- docs: The list of documents to be split into chunks.
- chunk_size: The size of each chunk of text (default value is 250).
- chunk_overlap: The number of characters to overlap between chunks (default value is 30).

**Code Description**:
The get_chunk_with_source function iterates through the input list of documents and splits each document into chunks using the split_documents function from utilities.py. It assigns a source metadata to each chunk based on the filename of the document. The function then aggregates all the splits and returns them as a single list of chunks with assigned sources.

This function is utilized in the project by functions such as set_vectorstore in the Model class to prepare document chunks for vectorization and by get_chunk_docs in the Model class to split a list of documents into chunks for further processing.

**Note**:
- Ensure the input documents are structured appropriately for accurate chunking.
- Adjust the chunk_size and chunk_overlap parameters as needed for specific chunking requirements.

**Output Example**:
```python
[
    Chunk 1: "Text chunk 1...",
    Chunk 2: "Text chunk 2...",
    ...
]
```
## FunctionDef filter_docs(docs)
**filter_docs**: The function of filter_docs is to filter a list of documents based on the presence of "summary.md" in the metadata source field.

**parameters**:
- docs: A list of documents to be filtered.

**Code Description**:
The `filter_docs` function takes a list of documents as input and filters out only those documents where the string "summary.md" is present in the metadata's 'source' field. It uses a list comprehension to iterate over the input list and return a new list containing only the filtered documents.

This function is called in the `__init__` method of the `DataGenerator` class in the `testset_generation.py` file. In this context, the function is used to filter the input documents and store the filtered documents in the `summary` attribute of the `DataGenerator` instance.

**Note**:
- Make sure the input documents have a 'metadata' field with a 'source' key to avoid any errors.
- The function is case-sensitive, so ensure that "summary.md" is written exactly as needed in the metadata source field.

**Output Example**:
If the input list of documents is as follows:
```python
docs = [
    {"name": "doc1", "metadata": {"source": "summary.md"}},
    {"name": "doc2", "metadata": {"source": "details.txt"}},
    {"name": "doc3", "metadata": {"source": "summary.md"}},
    {"name": "doc4", "metadata": {"source": "abstract.md"}}
]

filtered_docs = filter_docs(docs)
```

The `filtered_docs` will contain:
```python
[
    {"name": "doc1", "metadata": {"source": "summary.md"}},
    {"name": "doc3", "metadata": {"source": "summary.md"}}
]
```
## FunctionDef get_json_from_path(path)
**get_json_from_path**: The function of get_json_from_path is to load and return JSON data from a specified file path.

**parameters**:
- path: A string representing the file path from which JSON data will be loaded.

**Code Description**:
The get_json_from_path function opens the file specified by the path parameter in read mode with UTF-8 encoding. It then loads the JSON data from the file and returns it.

In the project, this function is called within the __init__ method of the Model class in the model.py file. The path_hierarchy parameter is passed to the get_json_from_path function to load JSON data from a specific file path.

**Note**:
It is important to ensure that the file specified by the path parameter exists and contains valid JSON data to prevent any errors during the loading process.

**Output Example**:
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
## FunctionDef get_qa_system_prompt
**get_qa_system_prompt**: The function of get_qa_system_prompt is to retrieve a prompt for question-answering tasks related to code documentation.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_qa_system_prompt function returns a specific prompt tailored for question-answering tasks related to code documentation. The prompt includes instructions for using the retrieved context to answer questions and mentions the file name containing the functions. This function is designed to assist in generating prompts for question-answering systems in a concise and structured manner.

In the project, this function is called within the set_chain method of the SpecificModel class. The prompt retrieved from get_qa_system_prompt is used to create prompt templates for the runnable chain, along with another prompt obtained from a different utility function. This highlights the integration of the get_qa_system_prompt function in the process of setting up the question-answering system within the specific model.

**Note**: Developers can utilize the get_qa_system_prompt function to obtain a standardized prompt for question-answering tasks related to code documentation, enhancing the efficiency and consistency of generating responses.

**Output Example**: 
"You are an assistant for question-answering tasks regarding code documentation file. Use the following pieces of retrieved context to answer the question. It's also specified the name of the file that contains the functions. If you don't know the answer, say that you don't know. Use three sentences maximum and keep the answer concise.
{context}"
## FunctionDef get_contextualize_q_system_prompt
**get_contextualize_q_system_prompt**: The function of get_contextualize_q_system_prompt is to formulate a standalone question based on a chat history and the latest user question, ensuring it can be understood without the context of the chat history.

**parameters**: 
This Function does not take any parameters.

**Code Description**: 
The get_contextualize_q_system_prompt function returns a reformulated question by considering a chat history and the latest user question. It ensures that the question can stand alone without the need for additional context. The function specifically focuses on reformulating the question without providing an answer, adding requests for more information, or seeking clarification beyond the original question.

This function is designed to be a part of a larger system that involves processing chat history and user questions to generate prompts for further interactions. In the project, this function is called by multiple ClassificationModel objects to set up prompts for contextualizing user questions within a chat context.

**Note**: 
Developers using this function should ensure that the returned question is standalone and does not require additional context to be understood. It is important to follow the guidelines of not answering the question, adding requests for more information, or seeking clarification beyond the original question.

**Output Example**: 
"Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question which can be understood without the chat history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is. Do NOT add requests for additional information or clarification if not in the original question. Keep it as a question."
## FunctionDef get_dont_contextualize_system_prompt
**get_dont_contextualize_system_prompt**: The function of get_dont_contextualize_system_prompt is to return a specific system prompt instructing not to add requests for additional information or clarification and not to answer the question.

**parameters**: This Function does not take any parameters.

**Code Description**: The get_dont_contextualize_system_prompt function returns a system prompt that advises to repeat the question as it is without adding requests for more information or answering the question.

In the project, this function is called in two different contexts:
1. In the GeneralModel class within the set_chain method, the prompt returned by get_dont_contextualize_system_prompt is used to set the prompt for creating a runnable chain.
2. In the SpecificModel class within the set_chain method, the prompt returned by get_dont_contextualize_system_prompt is used along with another prompt to create a runnable chain.

**Note**: Developers using this function should be aware that it provides a specific system prompt for handling questions without adding extra information or answering them directly.

**Output Example**: 
"Repeat the question as it is. Do NOT add requests for additional information or clarification if not in the original question. Do NOT answer the question."
## FunctionDef get_readme_path(root_path)
**get_readme_path**: The function of get_readme_path is to search for the README.md file in the root of a repository and return its path if found.

**parameters**:
- root_path: The root path of the repository to search for the README.md file.

**Code Description**:
The get_readme_path function starts by compiling a regular expression pattern to match README.md or README.txt files case-insensitively. It then normalizes and obtains the absolute path of the root directory. The function iterates through all files in the directory and its subdirectories using os.walk. If a file matches the pattern, the function returns the full path to that file. If no README file is found, it returns None.

This function is called in the load_docs method of the GeneralModel class in the general_model.py file. In this context, the function is used to determine the path of the README.md file in the repository root. If the README file is not found, an UnstructuredMarkdownLoader is initialized with a summary.md file. If the README file is found, the loader is initialized with the path to the README file. The loader then loads the documents, which are assigned to the docs attribute of the GeneralModel instance.

Additionally, the get_readme_path function is also called in the first_generate method of the Runner class in the runner.py file. In this scenario, the function is used to check if a README file exists in the target repository. If no README file is found, a ParallelSummarizator is created to generate a summary, which is then saved to a summary.md file in the markdown_docs_name directory of the target repository.

**Note**:
- The get_readme_path function is essential for locating the README.md file in a repository.
- It utilizes regular expressions to match README file names.
- The function returns the path to the README file if found, otherwise None.

**Output Example**:
If the README.md file is found in the root directory of the repository, the function may return: "/path/to/repository/README.md".
## FunctionDef load_docs(path_marksdown)
**load_docs**: The function of load_docs is to load documents from a specified path, process subdirectories, instantiate a loader for each subdirectory, and return a list of all loaded documents.

**parameters**:
- path_marksdown: The path to the markdown documents.

**Code Description**:
The load_docs function takes a path to markdown documents as input and proceeds to load all documents from the specified path. It normalizes the path to an absolute one and iterates through subdirectories using os.walk. For each subdirectory, it instantiates a DirectoryLoader with specific parameters such as the subdirectory, file extension, and loader class. The function then loads documents using the loader and appends them to the all_docs list. Any encountered exceptions during the loading process are caught and printed. Finally, the function returns a list containing all the loaded documents.

This function plays a crucial role in the document loading process within the chat_langchain utilities, enabling the retrieval of markdown documents for further processing in various components of the chatbot system.

**Note**:
- Ensure the provided path contains the necessary markdown documents for successful loading.
- Handle any exceptions that may arise during the document loading process to maintain the integrity of the operation.

**Output Example**:
```
[doc1, doc2, doc3, ...]
```
