## ClassDef Runner
**Runner**: The Runner class is responsible for generating and updating documentation for the target repository. It contains methods for generating documentation for individual objects, detecting changes in the repository, and running the document update process.

**Attributes**:
- `absolute_project_hierarchy_path`: The absolute path of the project hierarchy in the target repository.
- `project_manager`: An instance of the ProjectManager class, responsible for managing the project hierarchy and file operations.
- `change_detector`: An instance of the ChangeDetector class, used to detect changes in the repository.
- `chat_engine`: An instance of the ChatEngine class, responsible for generating documentation using a chat-based model.
- `meta_info`: An instance of the MetaInfo class, which stores the meta information of the documentation.
- `runner_lock`: A threading lock used to synchronize access to the Runner class.
- `summarizator`: An instance of the Summarizator class, used to generate a summary of the documentation.

**Code Description**:
The Runner class is the main class responsible for generating and updating documentation for the target repository. It initializes various components such as ProjectManager, ChangeDetector, ChatEngine, MetaInfo, Summarizator, and provides methods for generating documentation for individual objects, detecting changes in the repository, and running the document update process.

The `get_all_pys` method is used to retrieve all Python files in a given directory. It recursively searches the directory and its subdirectories, and returns a list of paths to all Python files.

The `generate_doc_for_a_single_item` method is used to generate documentation for a single object. It takes a DocItem object as input and uses the ChatEngine to generate the documentation content. The generated content is then appended to the DocItem's `md_content` attribute, and the DocItem's status is updated accordingly.

The `first_generate` method is used to generate all documents in the target repository. It initializes a task manager based on the meta information of the documentation, and generates documents in the specified order. The generated documents are synchronized back to the file system in real-time. If an error occurs during the generation process, it automatically loads and continues generating in the file order. After the generation is completed, the document version is updated and a summary of the documentation is generated.

The `markdown_refresh` method is used to write the latest document information to a folder in markdown format. It deletes all contents under the markdown folder and then rewrites them based on the meta information of the documentation.

The `git_commit` method is used to commit the changes made during the document update process.

The `run` method is the entry point for running the document update process. It detects changes in the repository, processes each changed file, and updates the documents accordingly. If it is the first time running the process, it generates all documents using the `first_generate` method. If it is not the first time, it checks for changes and updates the documents based on the changes detected.

**Note**: During the document update process, the target repository code should not be modified. The generation process of a document is bound to a specific version of the code.

**Output Example**: N/A
### FunctionDef __init__(self)
An unknown error occurred while generating this documentation after many tries.
***
### FunctionDef get_all_pys(self, directory)
**get_all_pys**: The function of get_all_pys is to retrieve all Python files within a specified directory.

**parameters**:
- directory: A string representing the directory path to search for Python files.

**Code Description**:
The get_all_pys function utilizes the os.walk method to traverse through the directory and its subdirectories. It checks each file encountered, and if the file has a ".py" extension, it appends the full path of the Python file to the python_files list. Finally, it returns the list of paths to all Python files found in the directory.

**Note**:
Ensure that the directory path provided is valid and accessible to avoid any FileNotFoundError exceptions.

**Output Example**:
['/path/to/file/example.py', '/path/to/another/file/test.py', ...]
***
### FunctionDef generate_doc_for_a_single_item(self, doc_item)
**generate_doc_for_a_single_item**: The function of `generate_doc_for_a_single_item` is to generate documentation for a given object. It takes a `DocItem` object as input, which contains information about the code, and performs the necessary steps to generate the documentation.

**Parameters**:
- `doc_item`: A `DocItem` object representing the documentation item to be generated.

**Code Description**:
The `generate_doc_for_a_single_item` function is responsible for generating documentation for a single object. It first checks if the object needs to be generated by calling the `need_to_generate` function. If the object does not need to be generated, the function prints a message indicating that the content is ignored or the document is already generated, and then returns.

If the object needs to be generated, the function proceeds to generate the documentation. It starts by retrieving the relative file path of the object using the `get_full_name` method of the `DocItem` object. It then checks if the object is in the ignore list by calling the `need_to_generate` function with the ignore list as a parameter. If the object is in the ignore list, the function prints a message indicating that the content is ignored, and then returns.

If the object is not in the ignore list, the function prints a message indicating that the document generation process has started. It creates a `FileHandler` object to handle file-related operations, such as reading and writing files. It also calls the `generate_doc` method of the `ChatEngine` object to generate the documentation for the object.

The `generate_doc` method takes the `doc_item` object and the `file_handler` object as input. It retrieves the necessary information from the `doc_item` object, such as the code type, name, content, and whether it has a return value. It also checks if the code is referenced by other objects or if it references other objects.

Next, the `generate_doc` method prepares prompts for the OpenAI chat model by combining the relevant information, such as the code type, name, content, and references. It handles cases where the total number of tokens in the prompts exceeds the model's limit by either trying a larger model or reducing the input length.

Once the prompts are prepared, the `generate_doc` method sends a request to the chat model to generate the documentation. It handles potential errors, such as API connection errors, by logging the errors, waiting for a specified time, and retrying the request. If the maximum number of attempts is reached without a successful response, the method either raises an exception or returns a predefined response message.

The generated documentation is then returned as a response message. If the code is referenced by other objects, the `generate_doc` method includes information about the objects that reference it and their corresponding code and documentation. Similarly, if the code references other objects, the method includes information about the objects that are referenced and their corresponding code and documentation. The method also provides a possible appearance of the code's return value as an output example.

Finally, the `generate_doc_for_a_single_item` function updates the `DocItem` object with the generated documentation and sets the item status to indicate that the documentation is up to date. It also checks the status of the document generation process and logs any errors that occur.

**Note**: The `generate_doc_for_a_single_item` function relies on the `ChatEngine` class and the `FileHandler` class to handle the generation of the documentation and the file-related operations, respectively. Developers can utilize this function to automatically generate documentation for code objects in their projects. By providing the necessary information and utilizing the OpenAI chat model, the function can generate detailed and accurate documentation, including information about references and return values.

Please note that the `generate_doc_for_a_single_item` function may encounter limitations in processing code that exceeds the model's token limit. In such cases, the function attempts to use larger models or reduce the input length to generate the documentation. However, if the code itself is too long to process, the function returns a predefined response message indicating the limitation.
***
### FunctionDef first_generate(self)
**first_generate**: The function of `first_generate` is to generate all the documents in the target repository. It ensures that the generation process is bound to a specific version of the code and handles errors and interruptions during the generation process.

**parameters**:
- None

**Code Description**:
The `first_generate` function is responsible for generating all the documents in the target repository. It starts by logging a message indicating the start of the documentation generation process.

The function then checks if the repository is already in the generation process by checking the `in_generation_process` attribute of the `meta_info` object. If it is not in the generation process, the function initializes a new task list. If it is in the generation process, the function loads the existing task list.

Next, the function prints the task list using the `print_task_list` method of the `meta_info` object. The task list displays the task ID, generation reason, path, and dependencies for each task.

The function creates a `task_manager` object using the `get_topology` method of the `meta_info` object. The `get_topology` method calculates the topological order of all objects in the repository based on the provided `check_task_available_func` function. This function determines whether a documentation item needs to be generated based on its status and other conditions.

The function then sets the `sync_func` attribute of the `task_manager` object to the `markdown_refresh` function. This function is responsible for refreshing the markdown documents by writing the latest document information to the target repository in markdown format.

The function creates multiple threads, each representing a worker, to perform the tasks assigned by the `task_manager`. Each worker calls the `worker` function, passing the `task_manager`, the process ID, and the `generate_doc_for_a_single_item` function as parameters. The `worker` function continuously performs tasks assigned by the `task_manager` until all tasks are successfully completed.

After the workers have completed their tasks, the function updates the `document_version` attribute of the `meta_info` object with the latest commit hash of the repository. It also sets the `in_generation_process` attribute of the `meta_info` object to `False` to indicate that the generation process is completed.

The function then calls the `checkpoint` method of the `meta_info` object to save the `MetaInfo` object and its associated metadata to the specified directory. This allows for easy retrieval and storage of document information.

If a summary is generated by the `summarizator` object, the function writes the summary to a file named "summary.md" in the markdown_docs_name folder of the target repository.

If any errors occur during the generation process, the function logs the error message and the number of documents generated at that time.

**Note**:
- The `first_generate` function generates all the documents in the target repository.
- It ensures that the generation process is bound to a specific version of the code.
- It handles errors and interruptions during the generation process.
- The `task_manager` object manages the tasks based on the topological order of the objects in the repository.
- The `worker` function performs the tasks assigned by the `task_manager`.
- The `markdown_refresh` function refreshes the markdown documents by writing the latest document information to the target repository in markdown format.
- The `checkpoint` method saves the `MetaInfo` object and its associated metadata to the specified directory.
- The `summarizator` object generates a summary of the documents.
- The function logs messages to provide updates on the generation process.
- Developers can use this function to generate all the documents in the target repository and ensure that the generation process is bound to a specific version of the code.

**Note**: During the `first_generate` process, the target repository code cannot be modified. The generation process of a document must be bound to a specific version of the code.
***
### FunctionDef markdown_refresh(self)
**markdown_refresh**: The function of markdown_refresh is to write the latest document information to a folder in markdown format, regardless of whether the markdown content has changed.

**parameters**:
- self: The current instance of the object.

**Code Description**:
The markdown_refresh function is a method of the current object. It is responsible for refreshing the markdown documents by writing the latest document information to the target repository in markdown format.

The function begins by acquiring a lock using the runner_lock attribute to ensure thread safety. It then proceeds to delete the existing contents under the markdown_docs_name folder in the target repository, if it exists, using the shutil.rmtree function. Afterward, it creates a new directory with the same name using the os.mkdir function.

Next, the function retrieves a list of all file items using the get_all_files method of the meta_info attribute. It then iterates through each file item in the list.

Within the iteration, the function defines a nested recursive function called recursive_check. This function is used to check if there is any documentation inside a file item. It recursively traverses the hierarchy of the file item and its children to determine if there is any markdown content. If no markdown content is found, the function continues to the next file item.

If markdown content is found, the function retrieves the relative file path of the file item using the get_full_name method. It then defines another nested recursive function called to_markdown. This function is responsible for converting a file item and its children into markdown format.

Inside the to_markdown function, the markdown_content variable is initialized as an empty string. The function constructs the markdown content by appending the appropriate markdown syntax based on the item's type, name, and content. It also handles the case where the item has parameters by appending them to the markdown content. Additionally, the function appends the last markdown content from the item's md_content attribute, or a placeholder message if the md_content is empty.

The function then recursively calls the to_markdown function for each child of the item, incrementing the now_level parameter by 1. After each recursive call, the function appends a horizontal rule syntax to separate the markdown content of different children.

Once the markdown content for a file item is generated, the function writes the content to a .md file in the markdown_docs_name folder. It constructs the file path by replacing the ".py" extension of the file item's name with ".md" and joining it with the markdown_docs_name folder path. The function creates any necessary directories in the file path using os.makedirs. Finally, it writes the markdown content to the .md file using the open function.

After processing all file items, the function logs a message indicating that the markdown documents have been refreshed at the markdown_docs_name folder.

**Note**:
- This function assumes that the setting.project.target_repo and setting.project.markdown_docs_name attributes are valid paths.
- The function relies on the meta_info attribute to retrieve file items and their hierarchical structure.
- The function uses the tqdm library to display a progress bar during the iteration over file items.
- The function assumes that the DocItem class has certain attributes and methods, such as md_content, children, get_full_name, get_file_name, and content.

**Output Example**:
If the markdown_refresh function is executed successfully, the following message will be logged:
"markdown document has been refreshed at {setting.project.markdown_docs_name}"
#### FunctionDef recursive_check(doc_item)
**recursive_check**: The function of recursive_check is to check if there is a document inside a file.

**parameters**:
- doc_item: DocItem - Represents the document item to be checked.

**Code Description**:
The recursive_check function takes a DocItem object as input and recursively checks if there is any markdown content stored in the md_content attribute of the DocItem. If the md_content is not empty, the function returns True. Otherwise, it iterates through the children of the DocItem and recursively calls itself on each child until a document with content is found or all children have been checked. If no document content is found in the DocItem or its children, the function returns False.

This function plays a crucial role in traversing through the hierarchical structure of DocItems to determine if any markdown content exists within the tree of objects.

**Note**:
Ensure that the input parameter is a valid DocItem object to avoid errors in the recursive checking process.

**Output Example**:
- True
- False
***
#### FunctionDef to_markdown(item, now_level)
**to_markdown**: The function of to_markdown is to generate markdown content based on the provided DocItem object and its children recursively.

**parameters**:
- item: Represents the DocItem object containing information to be converted to markdown.
- now_level: Indicates the current level in the hierarchy of the document.

**Code Description**: The to_markdown function constructs markdown content by processing the item and its children. It starts by creating a heading based on the item's type and name. If the item has parameters, they are included in the heading. The function then appends the last content from the item's md_content list or a default message if the list is empty. Next, it iterates over the item's children, recursively calling to_markdown to include their content in the markdown output. Each child's content is separated by a horizontal rule.

The function leverages the to_str method from the DocItemType class to determine the string representation of the item's type, which is used in the heading creation.

**Note**: It's essential to ensure that the DocItemType values are correctly defined to match the expected types in the to_str function. Any additional DocItemType values added in the future should be handled to prevent unexpected behavior.

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
It is important to ensure that the commit_message parameter is provided with a meaningful and descriptive message to accurately document the changes being committed to the repository. Additionally, this function relies on the subprocess module, so it is essential to handle any potential errors that may arise during the commit process.
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
The add_new_item function is responsible for adding new projects to the JSON file and generating the corresponding documentation. It takes two parameters: file_handler, which is an instance of the FileHandler class used for reading and writing files, and json_data, which is a dictionary containing the project structure information stored in the JSON file.

The function starts by initializing an empty dictionary called file_dict. This dictionary will store the information of all objects in the file. It then iterates through the functions and classes in the file using the get_functions_and_classes method of the file_handler object. For each object, it retrieves the code information using the get_obj_code_info method of the file_handler object. It then calls the generate_doc method of the chat_engine object to generate the documentation for the code. The generated documentation is stored in the md_content field of the code_info dictionary. The code_info dictionary is then added to the file_dict dictionary using the name of the object as the key.

After processing all objects in the file, the file_dict dictionary is added to the json_data dictionary using the file_handler's file_path as the key. The updated json_data dictionary is then written back to the JSON file.

Next, the function converts the updated part of the JSON file into markdown format using the convert_to_markdown_file method of the file_handler object. The markdown content is then written to a .md file using the write_file method of the file_handler object.

Finally, the function logs the completion of the JSON file update and the generation of the markdown documentation.

**Note**:
- Ensure that the file_handler object is properly initialized with the correct repo_path and file_path before calling this function.
- The function relies on the chat_engine object to generate the documentation for the code objects.
- The function assumes that the JSON file and the markdown documentation file have been properly set up before calling this function.
- Any changes made to the JSON file or the markdown documentation file will be reflected in the project structure and the generated documentation, respectively.

Please note that the provided documentation is based on the analysis of the code and its usage within the project.
***
### FunctionDef process_file_changes(self, repo_path, file_path, is_new_file)
**process_file_changes**: The function of `process_file_changes` is to handle the changes in a file by processing the file's content and updating the project hierarchy and markdown documentation accordingly.

**Parameters**:
- `self`: The object itself.
- `repo_path` (str): The path to the repository.
- `file_path` (str): The relative path to the file.
- `is_new_file` (bool): Indicates whether the file is new or not.

**Code Description**:
The `process_file_changes` function is called in the loop of detected changed files. Its purpose is to process changed files according to the absolute file path, including new files and existing files. 

The function first creates a `FileHandler` object to handle the file operations. It then reads the content of the file using the `read_file` method of the `FileHandler` object. The content is stored in the `source_code` variable.

Next, the function uses the `ChangeDetector` object to parse the differences in the file. It calls the `get_file_diff` method of the `ChangeDetector` object to retrieve the changes made to the file. The changes are stored in the `changed_lines` variable.

The function then calls the `identify_changes_in_structure` method of the `ChangeDetector` object to identify the changes in the file structure. It passes the `changed_lines` and the functions and classes extracted from the `source_code` to the method. The changes in the file structure are stored in the `changes_in_pyfile` variable.

The function logs the detected changes in the file structure using the `logger` object.

Next, the function checks if the file exists in the `project_hierarchy.json` file. If the file exists, it updates the JSON data with the changes in the file structure. It calls the `update_existing_item` method of the `Runner` class to update the existing item in the JSON data. If the file does not exist, it adds a new item to the JSON data. It calls the `add_new_item` method of the `Runner` class to add the new item to the JSON data.

After updating the JSON data, the function writes the updated JSON data back to the `project_hierarchy.json` file.

The function then converts the changes in the JSON data to markdown format. It calls the `convert_to_markdown_file` method of the `FileHandler` object to convert the changes to markdown format. The markdown content is stored in the `markdown` variable.

Finally, the function writes the markdown content to a `.md` file using the `write_file` method of the `FileHandler` object. It logs the completion of the JSON file update and the generation of the markdown documentation.

**Note**:
- Ensure that the `repo_path` and `file_path` parameters are correctly set before calling this function to process the file changes accurately.
- The function relies on the `FileHandler` and `ChangeDetector` objects to handle file operations and detect changes in the file structure, respectively.
- The function updates the project hierarchy and generates markdown documentation based on the changes in the file.
- Make sure to handle exceptions related to file operations and JSON manipulation appropriately.
- The function assumes that the `project_hierarchy.json` file and the markdown documentation file have been properly set up before calling this function.
***
### FunctionDef update_existing_item(self, file_dict, file_handler, changes_in_pyfile)
**update_existing_item**: The function of update_existing_item is to update the existing projects by modifying the file structure information dictionary based on the changes in the file.

**Parameters**:
- file_dict (dict): A dictionary containing the old object information.
- file_handler (FileHandler): The file handler object used to access the file.
- changes_in_pyfile (dict): A dictionary containing information about the objects that have changed in the file.

**Code Description**:
The `update_existing_item` function takes three parameters: `file_dict`, `file_handler`, and `changes_in_pyfile`. 

The `file_dict` parameter is a dictionary that contains the old object information. It represents the existing file structure information dictionary that needs to be updated.

The `file_handler` parameter is an instance of the `FileHandler` class, which provides access to the file and its content. It is used to retrieve the current file structure and update the file structure information dictionary.

The `changes_in_pyfile` parameter is a dictionary that contains information about the objects that have changed in the file. It includes two keys: "added" and "removed". The "added" key maps to a list of objects that have been added, while the "removed" key maps to a list of objects that have been removed.

The function first calls the `get_new_objects` method to retrieve the new and deleted objects based on the changes in the file. The `get_new_objects` method compares the current version and the previous version of the .py file to identify the added and deleted objects.

Next, the function processes the deleted objects by iterating through each object name in the `del_obj` list. If the object name exists in the `file_dict`, it is removed from the dictionary. A log message is also generated to indicate that the object has been deleted.

Then, the function generates the current file structure information by calling the `generate_file_structure` method of the `file_handler` object. This method reads the file content and extracts the file structure information, including the type, start line, end line, parent, and name column of each object.

The current file structure information is stored in the `current_info_dict` dictionary, where the object name is the key and the object information is the value.

The function then updates the global file structure information dictionary (`file_dict`) by iterating through each object in the `current_info_dict`. If the object name exists in the `file_dict`, its information is updated with the corresponding information from the `current_info_dict`. If the object name does not exist in the `file_dict`, the new object is added to the dictionary.

Next, the function retrieves the referencer list for each added object. It iterates through the added objects in the `changes_in_pyfile` dictionary and finds the corresponding object in the `current_objects` list. For each object, it calls the `find_all_referencer` method of the `project_manager` object to get the list of object referencers. The object name and its referencer list are then added to the `referencer_list`.

The function then uses a thread pool executor to concurrently update the objects. It iterates through each added object in the `changes_in_pyfile` dictionary and each referencer object in the `referencer_list`. If the object name matches the referencer object name, it submits a task to the executor to update the object using the `update_object` method. A log message is generated to indicate the progress of the documentation generation.

After all the tasks are submitted, the function waits for the tasks to complete using the `result` method of the `futures` object.

Finally, the function returns the updated file structure information dictionary (`file_dict`).

**Note**:
- The `file_dict` parameter should be a valid dictionary containing the old object information.
- The `file_handler` parameter should be an instance of the `FileHandler` class.
- The `changes_in_pyfile` parameter should be a dictionary with the "added" and "removed" keys.
- The `get_new_objects` method is called to identify the added and deleted objects based on the changes in the file.
- The `generate_file_structure` method is called to generate the current file structure information.
- The `find_all_referencer` method is called to retrieve the list of object referencers.
- The `update_object` method is called to generate the documentation content and update the corresponding field information of the object.
- The function utilizes a thread pool executor to improve performance by executing the tasks concurrently.
- The updated file structure information dictionary is returned as the output of the function.

**Output Example**:
{
    "object1": {
        "type": "function",
        "code_start_line": 10,
        "code_end_line": 20,
        "parent": "class1",
        "name_column": 5
    },
    "object2": {
        "type": "class",
        "code_start_line": 5,
        "code
***
### FunctionDef update_object(self, file_dict, file_handler, obj_name, obj_referencer_list)
**update_object**: The function of update_object is to generate documentation content and update the corresponding field information of the object.

**Parameters**:
- file_dict (dict): A dictionary containing old object information.
- file_handler: The file handler.
- obj_name (str): The object name.
- obj_referencer_list (list): The list of object referencers.

**Code Description**:
The `update_object` function is responsible for generating documentation content and updating the corresponding field information of the object. It takes several parameters, including `file_dict`, `file_handler`, `obj_name`, and `obj_referencer_list`.

The `file_dict` parameter is a dictionary that contains the old object information. It serves as a reference for retrieving the necessary information about the object.

The `file_handler` parameter represents the file handler object, which provides access to the project's files. It is used to retrieve and update the object's information.

The `obj_name` parameter is a string that specifies the name of the object to be updated. It is used to identify the object in the `file_dict` and retrieve its corresponding information.

The `obj_referencer_list` parameter is a list that contains the object referencers. It provides information about the objects that reference the code.

Within the function, the code first checks if the `obj_name` exists in the `file_dict`. If it does, the function retrieves the object's information and assigns it to the `obj` variable.

Next, the function calls the `generate_doc` function of the `ChatEngine` object to generate the documentation content. It passes the `obj`, `file_handler`, and `obj_referencer_list` as arguments to the `generate_doc` function.

The `generate_doc` function prepares prompts for the OpenAI chat model by combining relevant information such as the code type, name, content, and references. It handles cases where the total number of tokens in the prompts exceeds the model's limit by either trying a larger model or reducing the input length.

Once the prompts are prepared, the function sends a request to the chat model to generate the documentation. It handles potential errors, such as API connection errors, by logging the errors, waiting for a specified time, and retrying the request. If the maximum number of attempts is reached without a successful response, the function either raises an exception or returns a predefined response message.

The generated documentation is then returned as a response message. The function updates the `md_content` field of the `obj` with the content of the response message.

**Note**: It is important to note that the `generate_doc` function relies on the `ChatEngine` class and the `ResponseMessage` class to handle the generation of the documentation and the storage of response messages, respectively.

Developers can utilize the `update_object` function to automatically generate documentation for code objects in their projects. By providing the necessary information and utilizing the OpenAI chat model, the function can generate detailed and accurate documentation, including information about references and return values.

Please note that the `generate_doc` function may encounter limitations in processing code that exceeds the model's token limit. In such cases, the function attempts to use larger models or reduce the input length to generate the documentation. However, if the code itself is too long to process, the function returns a predefined response message indicating the limitation.
***
### FunctionDef get_new_objects(self, file_handler)
**get_new_objects**: The function of get_new_objects is to retrieve the added and deleted objects by comparing the current version and the previous version of a .py file.

**parameters**:
- file_handler (FileHandler): The file handler object used to retrieve the current and previous versions of the .py file.

**Code Description**:
The get_new_objects function takes a file_handler object as input and performs the following steps:

1. It calls the get_modified_file_versions function of the file_handler object to retrieve the current and previous versions of the .py file.
2. It calls the get_functions_and_classes function of the file_handler object to parse the current and previous versions of the .py file and retrieve a list of functions and classes present in each version.
3. It creates sets of the function and class names from the current and previous versions.
4. It calculates the added objects by finding the set difference between the current and previous object sets.
5. It calculates the deleted objects by finding the set difference between the previous and current object sets.
6. It converts the added and deleted object sets into lists.
7. It returns a tuple containing the added and deleted object lists.

The get_new_objects function is called in the update_existing_item function of the Runner class. In this context, it is used to compare the current and previous versions of a .py file and update the file structure information dictionary accordingly.

**Note**:
- The file_handler object should be properly initialized and contain the necessary file path information before calling this function.
- The get_modified_file_versions and get_functions_and_classes functions of the file_handler object should be implemented correctly to ensure accurate retrieval of file versions and parsing of code content.
- The function assumes that the file versions and code content provided are valid and can be processed without errors.

**Output Example**:
new_obj: ['add_context_stack', '__init__']
del_obj: []
***
