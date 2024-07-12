## ClassDef Runner
**Runner**: The Runner class is responsible for managing the document generation and update process.

**Attributes**:
- `absolute_project_hierarchy_path`: A string representing the absolute path of the project hierarchy.
- `project_manager`: An instance of the ProjectManager class responsible for managing the project.
- `change_detector`: An instance of the ChangeDetector class responsible for detecting changes in the repository.
- `chat_engine`: An instance of the ChatEngine class responsible for generating documentation using chat completion.
- `meta_info`: An instance of the MetaInfo class representing the meta information of the project.
- `runner_lock`: A threading.Lock object used for thread synchronization.

**Code Description**:
The Runner class encapsulates the functionality required for generating and updating documentation for the target repository. It initializes various objects and manages the document generation process.

The `__init__` method initializes the attributes of the Runner class. It sets the `absolute_project_hierarchy_path` attribute by concatenating the target repository path and the project hierarchy name. It creates instances of the ProjectManager, ChangeDetector, and ChatEngine classes, passing the necessary parameters. If the `absolute_project_hierarchy_path` does not exist, it calls the `make_fake_files` function to create fake files and initializes the `meta_info` attribute using the `init_meta_info` method of the MetaInfo class. It then calls the `checkpoint` method of the MetaInfo class to save the meta information to the target directory. If the `absolute_project_hierarchy_path` exists, it loads the meta information using the `from_checkpoint_path` method of the MetaInfo class.

The `get_all_pys` method takes a directory path as input and returns a list of paths to all Python files in the given directory. It uses the `os.walk` function to traverse the directory and checks if each file has a ".py" extension. It appends the paths of the Python files to the `python_files` list and returns it.

The `generate_doc_for_a_single_item` method generates documentation for a single object. It takes a `doc_item` parameter of type DocItem representing the object for which documentation needs to be generated. It calls the `generate_doc` method of the ChatEngine class, passing the `doc_item` and `file_handler` objects. It appends the generated documentation content to the `md_content` attribute of the `doc_item` and updates its `item_status` to DocItemStatus.doc_up_to_date. It then calls the `checkpoint` method of the MetaInfo class to save the updated meta information.

The `first_generate` method generates documentation for all objects in the target repository. It initializes a task manager using the `get_topology` method of the MetaInfo class, passing a check task available function. It checks if the `in_generation_process` attribute of the `meta_info` is False and sets it to True. It then prints the task list using the `print_task_list` method of the MetaInfo class. It creates multiple threads, each calling the `generate_doc_for_a_single_item` method with a task from the task manager. After all threads have completed, it updates the `document_version` attribute of the `meta_info` with the latest commit hash. It sets the `in_generation_process` attribute to False and calls the `checkpoint` method of the MetaInfo class to save the updated meta information. Finally, it logs the number of successfully generated documents.

The `markdown_refresh` method updates the markdown documents based on the latest document information. It first deletes all contents in the `markdown_docs_name` folder and creates a new folder. It retrieves all file items using the `get_all_files` method of the MetaInfo class. For each file item, it recursively checks if it has any documentation content. If it does, it generates markdown content using the `to_markdown` function. It then writes the markdown content to a `.md` file in the `markdown_docs_name` folder. Finally, it logs the completion of the markdown refresh process.

The `git_commit` method commits changes to the repository. It uses the `subprocess.check_call` function to execute the git commit command with the provided commit message.

The `run` method is the main entry point for the document update process. It first checks if the `document_version` attribute of the `meta_info` is empty. If it is, it calls the `first_generate` method to generate documentation for all objects in the target repository. It then calls the `checkpoint` method of the MetaInfo class to save the updated meta information. If the `in_generation_process` attribute of the `meta_info` is False, it starts the change detection process. It creates a new `new_meta_info` object using the `init_meta_info` method of the MetaInfo class and loads the document information from the `meta_info`. It then calls the `print_task_list` method of the MetaInfo class to print the task list. It creates multiple threads, each calling the `generate_doc_for_a_single_item` method
### FunctionDef __init__(self)
An unknown error occurred while generating this documentation after many tries.
***
### FunctionDef get_all_pys(self, directory)
**get_all_pys**: The function of get_all_pys is to retrieve all Python files within a specified directory.

**parameters**:
- directory: A string representing the directory path to search for Python files.

**Code Description**:
The get_all_pys function utilizes the os.walk method to traverse through the directory structure specified by the 'directory' parameter. It iterates over the files in each directory and appends the paths of files ending with ".py" to the 'python_files' list. Finally, it returns a list containing the paths to all Python files found in the directory.

**Note**:
It is essential to ensure that the 'directory' parameter provided is a valid directory path.

**Output Example**:
['/path/to/file1.py', '/path/to/file2.py', ...]
***
### FunctionDef generate_doc_for_a_single_item(self, doc_item)
**generate_doc_for_a_single_item**: The `generate_doc_for_a_single_item` function is responsible for generating documentation for a given object. It takes a `DocItem` object as input, which contains information about the code, and a `file_handler` object, which provides access to the project's files. The function retrieves the relative file path of the `DocItem` object and checks if it needs to be generated based on its status and the project's ignore list. If the `DocItem` object does not need to be generated, the function skips the document generation process. Otherwise, it prints a message indicating the start of the document generation and proceeds with the generation process.

The function uses the `chat_engine.generate_doc` method to generate the documentation. It passes the `DocItem` object and the `file_handler` object as parameters to the `generate_doc` method. The `generate_doc` method retrieves the necessary information from the `DocItem` object, such as the code type, name, content, and whether it has a return value. It also checks if the code is referenced by other objects or if it references other objects.

Next, the function prepares prompts for the OpenAI chat model by combining the relevant information, such as the code type, name, content, and references. It handles cases where the total number of tokens in the prompts exceeds the model's limit by either trying a larger model or reducing the input length.

Once the prompts are prepared, the function sends a request to the chat model to generate the documentation. It handles potential errors, such as API connection errors, by logging the errors, waiting for a specified time, and retrying the request. If the maximum number of attempts is reached without a successful response, the function either raises an exception or returns a predefined response message.

The generated documentation is then returned as a response message. If the code is referenced by other objects, the function includes information about the objects that reference it and their corresponding code and documentation. Similarly, if the code references other objects, the function includes information about the objects that are referenced and their corresponding code and documentation. The function also provides a possible appearance of the code's return value as an output example.

It is important to note that the `generate_doc_for_a_single_item` function relies on the `ChatEngine` class and the `ResponseMessage` class to handle the generation of the documentation and the storage of response messages, respectively.

Developers can utilize the `generate_doc_for_a_single_item` function to automatically generate documentation for code objects in their projects. By providing the necessary information and utilizing the OpenAI chat model, the function can generate detailed and accurate documentation, including information about references and return values.

Note: The `generate_doc_for_a_single_item` function may encounter limitations in processing code that exceeds the model's token limit. In such cases, the function attempts to use larger models or reduce the input length to generate the documentation. However, if the code itself is too long to process, the function returns a predefined response message indicating the limitation.
***
### FunctionDef first_generate(self)
**first_generate**: The function of `first_generate` is to generate documentation for all objects in the repository. It checks the status of each object and determines if it needs to be generated based on certain conditions. If the object needs to be generated, the function calls the `generate_doc_for_a_single_item` function to generate the documentation. After generating the documentation, the function updates the document version and saves the MetaInfo object.

**parameters**:
- self: The current instance of the object.

**Code Description**:
The `first_generate` function is responsible for generating documentation for all objects in the repository. It starts by logging an information message indicating the start of the documentation generation process.

The function then defines a `check_task_available_func` function using the `partial` function from the `functools` module. This function is used to determine if a documentation item needs to be generated based on its status and the project's ignore list.

Next, the function retrieves a `task_manager` object from the `meta_info` attribute. The `task_manager` object manages the tasks based on the topology of objects in the repository. It uses the `get_topology` method of the `meta_info` attribute to calculate the topological order of all objects in the repository. The `get_topology` method takes the `task_available_func` function as a parameter.

The function then checks if the `meta_info` object is in the generation process. If it is not, it sets the `in_generation_process` attribute of the `meta_info` object to `True` and logs an information message indicating the initialization of a new task list. If the `meta_info` object is already in the generation process, it logs an information message indicating the loading of an existing task list.

The function calls the `print_task_list` method of the `meta_info` object to print a table of task information. This table includes the task ID, generation reason, path, and dependencies for each task.

Inside a try-except block, the function sets the `sync_func` attribute of the `task_manager` object to the `markdown_refresh` method of the current object. This method is responsible for refreshing the markdown documents based on the latest document information.

The function then creates a list of threads, where each thread represents a worker. The number of threads is determined by the `max_thread_count` attribute from the `setting.project` module. Each thread calls the `worker` function, passing the `task_manager`, the process ID, and the `generate_doc_for_a_single_item` function as parameters.

The function starts each thread and waits for them to finish using the `join` method. Once all threads have finished, the function updates the document version of the `meta_info` object with the commit hash of the current repository head. It sets the `in_generation_process` attribute of the `meta_info` object to `False` and calls the `checkpoint` method of the `meta_info` object to save the `MetaInfo` object to the specified directory.

Finally, the function logs an information message indicating the number of documents successfully generated during the process.

**Note**:
- The `first_generate` function is used to generate documentation for all objects in the repository.
- It checks the status of each object and determines if it needs to be generated based on certain conditions.
- The `check_task_available_func` function is used to determine if a documentation item needs to be generated based on its status and the project's ignore list.
- The `task_manager` object manages the tasks based on the topology of objects in the repository.
- The `print_task_list` method prints a table of task information, providing an overview of the tasks to be executed.
- The `sync_func` attribute of the `task_manager` object is set to the `markdown_refresh` method to refresh the markdown documents.
- Multiple threads are used to perform the tasks assigned by the `task_manager` object in parallel.
- The document version is updated and the `MetaInfo` object is saved after the generation process.
- The `checkpoint` method saves the `MetaInfo` object to the specified directory.
- The `markdown_refresh` method is called to update the markdown documents based on the latest document information.

**Note**: The `first_generate` function is an important part of the document generation process. It ensures that all objects in the repository are properly documented and up to date. Developers can use this function to generate documentation for their projects and keep track of the document version and status.
***
### FunctionDef markdown_refresh(self)
**markdown_refresh**: The function of markdown_refresh is to write the latest document information to a markdown format folder, regardless of whether the markdown content has changed or not.

**parameters**:
- self: The current instance of the object.

**Code Description**:
The markdown_refresh function is a method of the current object. It is responsible for updating the markdown documents based on the latest document information. The function first acquires a lock using the runner_lock attribute to ensure that the process is thread-safe.

Next, the function retrieves the target folder for the markdown documents by concatenating the target_repo and markdown_docs_name attributes from the setting.project module. If the markdown folder already exists, it is deleted using the shutil.rmtree function to remove all its contents. Then, a new directory is created using the os.mkdir function.

The function then retrieves a list of all file items using the get_all_files method of the meta_info attribute. It iterates through each file item and checks if it contains any documentation by calling the recursive_check function.

The recursive_check function is a nested function defined within the markdown_refresh function. It takes a DocItem object as a parameter and recursively checks if the object or its children contain any documentation. It returns True if documentation is found, and False otherwise.

If a file item does not contain any documentation, it is skipped. Otherwise, the function retrieves the relative file path using the get_full_name method of the file_item. 

The function then defines another nested function called to_markdown, which takes a DocItem object and the current level as parameters. This function is responsible for converting a DocItem object and its children into markdown format. It starts by initializing an empty string called markdown_content. It then appends the appropriate number of "#" characters based on the current level, followed by the item type and object name. If the item has parameters, they are appended in parentheses. The function then appends the last element of the item's md_content list, which represents the documentation content. 

Next, the function iterates through each child of the item and recursively calls the to_markdown function. The markdown content of each child is appended to the markdown_content string, followed by "***" as a separator.

After defining the to_markdown function, the markdown_refresh function initializes an empty string called markdown. It then iterates through each child of the file_item and calls the to_markdown function, passing the child and a level of 2. The markdown content of each child is appended to the markdown string.

The function asserts that the markdown string is not empty, and if it is, an AssertionError is raised with the file path of the file_item.

Next, the function constructs the file path for the markdown file by replacing the ".py" extension of the file_item's file name with ".md". It then checks if the file path starts with a "/", and if it does, removes the leading "/". The absolute file path is obtained by concatenating the target_repo and file path.

The function creates the necessary directories using os.makedirs, ensuring that the parent directories exist. It then opens the markdown file in write mode using the open function and writes the markdown content to the file.

Finally, the function logs an information message indicating that the markdown document has been refreshed at the markdown_docs_name folder.

**Note**:
- The markdown_refresh function updates the markdown documents based on the latest document information.
- It acquires a lock to ensure thread safety.
- The function deletes the existing markdown folder and creates a new one.
- It retrieves a list of all file items and checks if they contain documentation.
- The function converts each file item and its children into markdown format using the to_markdown function.
- The markdown content is written to the corresponding markdown file.
- The function logs an information message after the markdown documents have been refreshed.

**Output Example**:
If the markdown_docs_name folder is "docs" and the file_item represents a file named "example.py" with the following documentation content:

```
# Class Example
This is an example class.
```

The markdown_refresh function will create a file named "example.md" in the "docs" folder with the following content:

```
## Class Example
This is an example class.
```
#### FunctionDef recursive_check(doc_item)
**recursive_check**: The function of recursive_check is to check if a file contains documentation by recursively traversing through its children.

**parameters**:
- doc_item: DocItem - The DocItem object representing the file to be checked for documentation.

**Code Description**:
The recursive_check function takes a DocItem object as input and checks if the file represented by the DocItem object contains documentation. It recursively traverses through the children of the DocItem object to determine if any of them contain documentation. If documentation is found in any of the children or the original DocItem object, the function returns True. Otherwise, it returns False.

This function plays a crucial role in the documentation generation process by ensuring that all relevant files are checked for documentation content.

**Note**:
- This function relies on the DocItem class to access information about the file structure and content.
- It is designed to be used within the context of a documentation generation system to verify the presence of documentation in files.

**Output Example**:
True
***
#### FunctionDef to_markdown(item, now_level)
**to_markdown**: The function of to_markdown is to generate markdown content based on the provided DocItem object and its children recursively.

**parameters**:
- item: Represents a DocItem object containing information about a specific item.
- now_level: Indicates the current level of the item in the hierarchy.

**Code Description**: The to_markdown function constructs markdown content by processing the information stored in the DocItem object and its children. It starts by creating a header based on the item's type and name. If the item has parameters, they are included in the header. The function then appends the last content of the item (if available) and recursively processes its children to generate a hierarchical markdown structure. Each child is processed with an increased level indicator to maintain the hierarchy. A horizontal rule is added after each child's content.

The function utilizes the to_str method from the DocItemType class to convert the item's type to a string representation. This conversion helps in including the type information in the generated markdown content.

**Note**: It is crucial to ensure that the DocItemType values are correctly defined to match the expected types in the to_str function. Any additional DocItemType values added in the future should be handled to prevent unexpected behavior.

**Output Example**: 
```
# ClassDef ExampleClass
Class documentation content...

***
## FunctionDef example_function(param1, param2)
Function documentation content...

***
```
***
***
### FunctionDef git_commit(self, commit_message)
**git_commit**: The function of git_commit is to commit changes to a Git repository with a specified commit message.

**parameters**:
- commit_message: A string representing the message for the commit.

**Code Description**:
The git_commit function utilizes the subprocess module to execute a Git commit command with the provided commit message. It attempts to commit changes to the Git repository using the specified message. If the commit operation encounters an error, it catches the subprocess.CalledProcessError exception and prints an error message indicating the failure.

**Note**:
Developers using this function should ensure that the commit_message parameter is provided as a string to describe the changes being committed to the repository. Additionally, they should handle any potential errors that may arise during the commit process.
***
### FunctionDef run(self)
An unknown error occurred while generating this documentation after many tries.
***
### FunctionDef add_new_item(self, file_handler, json_data)
**add_new_item**: The function of add_new_item is to add new projects to the JSON file and generate corresponding documentation.

**parameters**:
- file_handler (FileHandler): The file handler object for reading and writing files.
- json_data (dict): The JSON data storing the project structure information.

**Code Description**:
The add_new_item function is responsible for adding new projects to the JSON file and generating the corresponding documentation. It takes two parameters: file_handler, which is an object that handles file operations such as reading and writing, and json_data, which is a dictionary that stores the project structure information.

Within the function, a file_dict is created to store the objects within the file. The function iterates through the objects in the file using the get_functions_and_classes method of the file_handler object. For each object, it retrieves the code information using the get_obj_code_info method of the file_handler object. It then generates documentation for the code using the generate_doc method of the chat_engine object. The generated documentation is stored in the md_content field of the code_info dictionary.

The file_dict is updated with the code_info dictionary, using the name of the object as the key. The json_data dictionary is updated with the file_dict, using the file_handler.file_path as the key. The updated json_data is then written back to the JSON file.

Next, the function converts the updated json_data into markdown format using the convert_to_markdown_file method of the file_handler object. The markdown content is then written to a .md file using the write_file method of the file_handler object.

Finally, the function logs the completion of the process by outputting the file path and the corresponding actions taken.

**Note**:
- Ensure that the file_handler object is properly initialized with the correct repo_path and file_path.
- The function relies on the file_handler object to read and write files, as well as retrieve code information and convert it to markdown format.
- The json_data dictionary should contain the necessary project structure information before calling this function.
- The function updates the json_data and writes it back to the JSON file, as well as generates and writes the markdown documentation for the new projects.
- It is important to note that the function relies on the chat_engine object to generate the documentation for the code objects. Ensure that the chat_engine object is properly initialized and configured before calling this function.


***
### FunctionDef process_file_changes(self, repo_path, file_path, is_new_file)
**process_file_changes**: The function of `process_file_changes` is to process changed files according to the absolute file path, including new files and existing files. It takes the `repo_path`, `file_path`, and `is_new_file` as input parameters. The `repo_path` is the path to the repository, `file_path` is the relative path to the file, and `is_new_file` indicates whether the file is new or not.

The function begins by creating a `FileHandler` object, `file_handler`, to handle file operations for the changed file. It then reads the content of the file using the `read_file` method of the `file_handler`. 

Next, the function uses the `change_detector` object to parse the differences in the file using the `parse_diffs` method. It retrieves the changed lines and identifies the changes in the file structure using the `identify_changes_in_structure` method. The changes in the file structure are stored in the `changes_in_pyfile` dictionary.

The function then checks if the file exists in the `project_hierarchy.json` file. If it does, it updates the JSON file with the changes in the file structure and writes the updated file back to the JSON file. It also converts the changes in the file structure to markdown format using the `convert_to_markdown_file` method of the `file_handler` and writes the markdown content to a `.md` file.

If the file does not exist in the `project_hierarchy.json` file, the function adds a new item to the JSON file using the `add_new_item` method of the `Runner` class.

Finally, the function adds the modified Markdown files to the staging area using the `add_unstaged_files` method of the `change_detector` object.

**Note**:
- Ensure that the `repo_path` and `file_path` parameters are correctly provided.
- The function relies on the `FileHandler`, `change_detector`, and `project_manager` objects to perform file operations, parse differences, and manage the project hierarchy.
- The function updates the project hierarchy JSON file and generates Markdown documentation for the changed files.
- Handle exceptions related to file operations and subprocess calls appropriately.
***
### FunctionDef update_existing_item(self, file_dict, file_handler, changes_in_pyfile)
**update_existing_item**: The function of update_existing_item is to update the existing projects by making changes to the file structure information dictionary based on the provided file dictionary, file handler, and changes in the Python file.

**Parameters**:
- file_dict (dict): A dictionary containing the file structure information.
- file_handler (FileHandler): The file handler object used to access file-related operations.
- changes_in_pyfile (dict): A dictionary containing information about the objects that have changed in the Python file.

**Code Description**:
The `update_existing_item` function is responsible for updating the existing projects by making changes to the file structure information dictionary. It takes three parameters: `file_dict`, `file_handler`, and `changes_in_pyfile`.

First, the function calls the `get_new_objects` function to retrieve the new and deleted objects based on the provided file handler. The new objects are stored in the `new_obj` variable, and the deleted objects are stored in the `del_obj` variable.

Next, the function iterates through the deleted objects and removes them from the `file_dict` if they exist. It also logs a message indicating that the object has been deleted.

Then, the function generates the current file structure information by calling the `generate_file_structure` function of the `file_handler` object. It retrieves the current objects and stores them in the `current_objects` variable.

The function creates a dictionary called `current_info_dict` to store the current object information using the object name as the key and the object information as the value.

Next, the function updates the global file structure information in the `file_dict` by iterating through the current object information. If the current object exists in the `file_dict`, its information is updated with the corresponding information from the `current_info_dict`. If the current object does not exist in the `file_dict`, it is added to the `file_dict`.

Then, the function iterates through the added objects in the `changes_in_pyfile` and retrieves the referencer list for each object by calling the `find_all_referencer` function of the `project_manager` object. The object name and its referencer list are stored in the `referencer_list`.

The function uses a `ThreadPoolExecutor` to concurrently update the objects in the `changes_in_pyfile`. For each added object, it retrieves the corresponding referencer list from the `referencer_list` and submits a task to the executor to update the object by calling the `update_object` function.

Finally, the function returns the updated `file_dict`.

**Note**:
- The `file_dict` parameter should be a dictionary containing the file structure information.
- The `file_handler` parameter should be a valid `FileHandler` object.
- The `changes_in_pyfile` parameter should be a dictionary containing information about the objects that have changed in the Python file.
- The `get_new_objects` function is called to retrieve the new and deleted objects.
- The `generate_file_structure` function is called to generate the current file structure information.
- The `find_all_referencer` function is called to retrieve the referencer list for each added object.
- The `update_object` function is called to update each added object.
- The function uses a `ThreadPoolExecutor` to improve performance by executing tasks concurrently.

**Output Example**:
{
    "function_name": {
        "type": "function",
        "code_start_line": 10,
        "code_end_line": 20,
        "parent": "class_name",
        "name_column": 5
    },
    "class_name": {
        "type": "class",
        "code_start_line": 5,
        "code_end_line": 25,
        "parent": None,
        "name_column": 10
    }
}
***
### FunctionDef update_object(self, file_dict, file_handler, obj_name, obj_referencer_list)
**update_object**: The function of update_object is to generate documentation content and update the corresponding field information of the object.

**Parameters**:
- file_dict (dict): A dictionary containing old object information.
- file_handler: The file handler.
- obj_name (str): The object name.
- obj_referencer_list (list): The list of object referencers.

**Code Description**:
The `update_object` function is responsible for generating documentation content and updating the corresponding field information of the object. It takes several parameters, including `file_dict`, which is a dictionary containing the old object information, `file_handler`, which is the file handler object, `obj_name`, which is the name of the object, and `obj_referencer_list`, which is a list of object referencers.

The function first checks if the `obj_name` exists in the `file_dict`. If it does, it retrieves the object from the dictionary and assigns it to the `obj` variable. 

Next, the function calls the `generate_doc` function of the `ChatEngine` object to generate the documentation for the `obj`. It passes the `obj`, `file_handler`, and `obj_referencer_list` as arguments to the `generate_doc` function. The generated documentation is stored in the `response_message` variable.

Finally, the function updates the `md_content` field of the `obj` with the content of the `response_message`.

**Note**:
- The `update_object` function relies on the `generate_doc` function of the `ChatEngine` class to generate the documentation.
- The `update_object` function updates the `md_content` field of the object with the generated documentation.
- It is important to ensure that the necessary parameters are provided when calling the `update_object` function.
- The function does not return any value.
***
### FunctionDef get_new_objects(self, file_handler)
**get_new_objects**: The function of get_new_objects is to retrieve the added and deleted objects by comparing the current version and the previous version of a .py file.

**parameters**:
- file_handler (FileHandler): The file handler object used to access file-related operations.

**Code Description**:
The get_new_objects function takes a file_handler object as input and performs the following steps:

1. It calls the get_modified_file_versions function of the file_handler object to retrieve the current and previous versions of the .py file.
2. It calls the get_functions_and_classes function of the file_handler object to parse the current and previous versions of the .py file and retrieve all functions and classes along with their parameters and hierarchical relationships.
3. It creates sets of the names of functions and classes in the current and previous versions.
4. It calculates the added objects by subtracting the previous object set from the current object set and converts the result to a list.
5. It calculates the deleted objects by subtracting the current object set from the previous object set and converts the result to a list.
6. It returns a tuple containing the added objects and deleted objects.

The get_new_objects function is called within the update_existing_item function of the Runner class. It is used to identify the added and deleted objects in a .py file and update the file structure information dictionary accordingly.

**Note**:
- The get_modified_file_versions function is called to retrieve the current and previous versions of the .py file.
- The get_functions_and_classes function is called to parse the current and previous versions of the .py file and retrieve the functions and classes.
- The function assumes that the file_handler object is correctly initialized and the necessary file operations are implemented.
- The function assumes that the get_modified_file_versions and get_functions_and_classes functions return the expected data structures.

**Output Example**:
new_obj: ['add_context_stack', '__init__']
del_obj: []
***
