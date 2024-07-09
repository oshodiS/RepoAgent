## ClassDef FileHandler
**FileHandler**: The function of FileHandler is to handle file-related operations in the repository.

**Attributes**:
- `repo_path`: The path to the repository.
- `file_path`: The relative path to the file.
- `project_hierarchy`: The path to the project hierarchy file.

**Code Description**:
The `FileHandler` class provides methods to perform various file operations in the repository. It is primarily used for reading and writing file content, retrieving code information, generating file structures, and converting file content to markdown format.

The `__init__` method initializes the `FileHandler` object with the repository path and file path. It also sets the `project_hierarchy` attribute to the path of the project hierarchy file.

The `read_file` method reads the content of the current file and returns it as a string.

The `get_obj_code_info` method retrieves code information for a given object. It takes the code type, code name, start line, end line, and parameters as input. It returns a dictionary containing the code information.

The `write_file` method writes the provided content to a file. It takes the file path and content as input.

The `get_modified_file_versions` method retrieves the current and previous versions of the modified file. It uses the `git` library to access the repository and retrieve the file versions.

The `get_end_lineno` method returns the end line number of a given node in the Abstract Syntax Tree (AST). It recursively traverses the AST to find the maximum end line number.

The `add_parent_references` method adds a parent reference to each node in the AST. It recursively traverses the AST and sets the parent attribute of each child node to the current node.

The `get_functions_and_classes` method retrieves all functions and classes in the code content. It takes the code content as input and returns a list of tuples containing the type of the node, the name of the node, the starting line number, the ending line number, the name of the parent node, and a list of parameters (if any).

The `generate_file_structure` method generates the file structure for the given file path. It reads the file content, retrieves the functions and classes, and returns a list of dictionaries containing the code information.

The `generate_overall_structure` method generates the overall file structure for the repository. It takes the file path reflections and jump files as input and returns a dictionary containing the file path and the generated file structure.

The `convert_to_markdown_file` method converts the content of a file to markdown format. It takes an optional file path as input and returns the content of the file in markdown format.

**Note**: The `FileHandler` class is designed to handle file-related operations in the repository. It provides methods to read and write file content, retrieve code information, generate file structures, and convert file content to markdown format. It relies on the `git` library for version control operations.
### FunctionDef __init__(self, repo_path, file_path)
**__init__**: The function of __init__ is to initialize the object with the provided repo_path and file_path.

**parameters**:
- repo_path: The path of the repository.
- file_path: The path relative to the root directory of the repository.

**Code Description**:
In this function, the provided repo_path and file_path are assigned to the object's attributes self.repo_path and self.file_path respectively. Additionally, the project_hierarchy attribute is set by combining the target repository path and the hierarchy name specified in the settings.

**Note**:
- Make sure to provide valid paths for repo_path and file_path when initializing the object.
***
### FunctionDef read_file(self)
**read_file**: The function of read_file is to read the content of the current changed file.

**parameters**:
- self: The object itself.

**Code Description**: The read_file function reads the content of the file specified by the repo_path and file_path attributes of the object. It first constructs the absolute file path using os.path.join, then opens the file in read mode with utf-8 encoding, reads the content, and returns it.

This function is called within the Runner class in the process_file_changes method. In this method, after detecting changes in a file, read_file is used to retrieve the content of the file. The content is then processed further based on the changes identified in the file.

**Note**: Ensure that the repo_path and file_path attributes are correctly set before calling this function to read the desired file.

**Output Example**: 
"The content of the current changed file."
***
### FunctionDef get_obj_code_info(self, code_type, code_name, start_line, end_line, params, file_path)
**get_obj_code_info**: The function of get_obj_code_info is to retrieve detailed information about a specific code object within a file.

**parameters**:
- code_type (str): The type of the code.
- code_name (str): The name of the code.
- start_line (int): The starting line number of the code.
- end_line (int): The ending line number of the code.
- params (str): The parameters of the code.
- file_path (str, optional): The file path. Defaults to None.

**Code Description**:
The get_obj_code_info function takes input parameters such as the type of code, code name, start and end line numbers, parameters, and an optional file path. It then reads the specified file, extracts the code content based on the provided line numbers, identifies the position of the code name in the content, checks for the presence of a return statement, and constructs a dictionary containing detailed information about the code object. This function is crucial for analyzing and documenting code objects within a file.

In the project, this function is called by other objects such as generate_file_structure and add_new_item to gather code information for different code objects within files. The generated code information is used for various purposes like generating documentation, updating JSON data, and converting content to markdown format.

**Note**:
- Ensure that the provided file path is correct to access the code file.
- The function relies on accurate line numbers to extract the code content effectively.

**Output Example**:
{
    "type": "function",
    "name": "example_function",
    "md_content": [],
    "code_start_line": 10,
    "code_end_line": 20,
    "params": "param1, param2",
    "have_return": True,
    "code_content": "def example_function(param1, param2):\n    return result",
    "name_column": 4
}
***
### FunctionDef write_file(self, file_path, content)
**write_file**: The function of write_file is to write the provided content to a file specified by the file path.

**parameters**:
- file_path (str): The relative path of the file.
- content (str): The content to be written to the file.

**Code Description**:
The `write_file` function first ensures that the `file_path` is a relative path by removing any leading '/'. It then constructs the absolute file path by joining the repository path with the adjusted file path. Directories along the file path are created if they do not exist. The function then opens the file in write mode with UTF-8 encoding and writes the content to the file.

In the project, the `write_file` function is called within the `add_new_item` and `process_file_changes` functions of the `Runner` class in the `runner.py` file. In the `add_new_item` function, after generating documentation for a newly added file, the `write_file` function is used to write the generated markdown content to a corresponding `.md` file. Similarly, in the `process_file_changes` function, the `write_file` function is utilized to update the markdown content of an existing file after making structural changes.

**Note**:
Ensure that the `file_path` provided is a relative path.
The function overwrites the existing content of the file with the new content.
***
### FunctionDef get_modified_file_versions(self)
**get_modified_file_versions**: The function of get_modified_file_versions is to retrieve the current and previous versions of a modified file.

**parameters**: 
- None

**Code Description**: 
The get_modified_file_versions function first initializes a Git repository object using the provided repo_path. It then reads the current version of the file by opening and reading the file located at repo_path/file_path. Next, it retrieves the previous version of the file by accessing the file version from the last commit using GitPython library. If there are commits available, it reads the previous version; otherwise, it sets the previous version to None. Finally, it returns a tuple containing the current version and the previous version of the file.

In the project, this function is called by the get_new_objects function in the Runner class. The get_new_objects function utilizes the output of get_modified_file_versions to compare the added and deleted objects in the current and previous versions of a Python file.

**Note**: 
- This function requires the GitPython library to be installed.
- Ensure that the repo_path and file_path are correctly set before calling this function.

**Output Example**: 
(current_version, previous_version)
***
### FunctionDef get_end_lineno(self, node)
**get_end_lineno**: The function of get_end_lineno is to retrieve the end line number of a given node in the code abstract syntax tree (AST).

**parameters**:
- node: The node for which to find the end line number.

**Code Description**: 
The get_end_lineno function first checks if the given node has a line number attribute. If the node does not have a line number, it returns -1. Otherwise, it iterates through the child nodes of the given node to find the end line number recursively. It updates the end line number only when a child node has a valid line number, ensuring that the final end line number is the maximum of all child nodes' end line numbers.

In the context of the project, the get_end_lineno function is utilized within the get_functions_and_classes method of the FileHandler class. It is called to determine the end line number of a node (e.g., FunctionDef, ClassDef) while parsing the code content of a file. This information is crucial for identifying the scope and boundaries of functions and classes in the code.

**Note**: 
- The function returns -1 if the node does not have a line number.
- The end line number is determined by considering the end line numbers of all child nodes recursively.

**Output Example**: 
If the end line number of a given node is 42, the function will return:
```python
42
```
***
### FunctionDef add_parent_references(self, node, parent)
**add_parent_references**: The function of add_parent_references is to add a parent reference to each node in the Abstract Syntax Tree (AST).

**parameters**:
- node: The current node in the AST.
- parent: The parent node in the AST (default is None).

**Code Description**:
The add_parent_references function iterates through each child node of the given node in the AST using the ast.iter_child_nodes method. It assigns the parent node as the current node to each child node by setting child.parent = node. This process is recursive, as it calls itself with the child node and the parent node. This way, a parent reference is added to each node in the AST, establishing hierarchical relationships between nodes.

In the calling object get_functions_and_classes, the add_parent_references function is used to add parent references to the nodes in the AST parsed from the code content. This allows for the retrieval of functions, classes, their parameters, and their hierarchical relationships accurately. The function then walks through the AST nodes, identifies FunctionDef, ClassDef, and AsyncFunctionDef nodes, retrieves relevant information such as node names, start and end line numbers, and parameters, and constructs a list of tuples representing these nodes and their details.

**Note**: It is essential to call add_parent_references before walking through the AST to ensure that parent references are correctly assigned to each node for accurate hierarchical analysis.
***
### FunctionDef get_functions_and_classes(self, code_content)
**get_functions_and_classes**: The function of get_functions_and_classes is to retrieve all functions, classes, their parameters (if any), and their hierarchical relationships from the code content of a file.

**parameters**:
- code_content: The code content of the whole file to be parsed.

**Code Description**: 
The get_functions_and_classes function takes the code content of a file as input and parses it using the ast module to generate an Abstract Syntax Tree (AST). It then iterates through the nodes in the AST and identifies FunctionDef, ClassDef, and AsyncFunctionDef nodes. For each of these nodes, it retrieves relevant information such as the node type, name, starting line number, ending line number, and parameters (if any). It constructs a list of tuples representing these nodes and their details.

To accurately determine the end line number of a node, the function calls the get_end_lineno function, which retrieves the end line number of a given node in the AST. This information is crucial for identifying the scope and boundaries of functions and classes in the code.

The add_parent_references function is also called within get_functions_and_classes to add parent references to the nodes in the AST. This allows for the retrieval of hierarchical relationships between nodes, such as a function being nested within a class.

The get_functions_and_classes function returns a list of tuples, where each tuple contains the type of the node (FunctionDef, ClassDef, AsyncFunctionDef), the name of the node, the starting line number, the ending line number, the name of the parent node (if any), and a list of parameters (if any).

**Note**: 
- The function uses the ast module to parse the code content and generate an AST.
- The get_end_lineno function is called to determine the end line number of a node.
- The add_parent_references function is called to add parent references to the nodes in the AST.
- The function returns a list of tuples representing the functions, classes, and their details in the code.

**Output Example**: 
If the code content contains a function named "AI_give_params" starting at line 86 and ending at line 95, a class named "PipelineEngine" starting at line 97 and ending at line 104, and a function named "get_all_pys" starting at line 99 and ending at line 104, the function will return:
[('FunctionDef', 'AI_give_params', 86, 95, None, ['param1', 'param2']), ('ClassDef', 'PipelineEngine', 97, 104, None, []), ('FunctionDef', 'get_all_pys', 99, 104, 'PipelineEngine', ['param1'])]
***
### FunctionDef generate_file_structure(self, file_path)
**generate_file_structure**: The function of generate_file_structure is to generate the file structure for the given file path.

**parameters**:
- file_path (str): The relative path of the file.

**Code Description**:
The generate_file_structure function takes a file path as input and reads the content of the specified file. It then calls the get_functions_and_classes function to retrieve all functions and classes from the code content. For each function or class, it calls the get_obj_code_info function to gather detailed information about the code object. The function constructs a list of dictionaries containing the code information for each object and returns it.

The function is an essential part of the file handling process in the project. It is called by the generate_overall_structure function to generate the file structure information for all files in the repository. The generated file structure information is used for various purposes, such as generating documentation, updating JSON data, and converting content to markdown format.

**Note**:
- Ensure that the provided file path is correct to access the code file.
- The function relies on the get_functions_and_classes and get_obj_code_info functions to gather code information effectively.

**Output Example**:
{
    "function_name": {
        "type": "function",
        "start_line": 10,
        ··· ···
        "end_line": 20,
        "parent": "class_name"
    },
    "class_name": {
        "type": "class",
        "start_line": 5,
        ··· ···
        "end_line": 25,
        "parent": None
    }
}
***
### FunctionDef generate_overall_structure(self, file_path_reflections, jump_files)
**generate_overall_structure**: The function of generate_overall_structure is to retrieve the file structure and object information for a target repository. It uses the AST-walk technique to parse the code and extract all objects. The function skips certain files based on the provided jump_files parameter and generates the file structure information for the remaining files.

**parameters**:
- file_path_reflections (dict): A dictionary containing the reflections of file paths.
- jump_files (list): A list of files to be skipped during the file structure generation process.

**Code Description**:
The generate_overall_structure function takes two parameters: file_path_reflections and jump_files. It initializes an empty dictionary called repo_structure to store the file structure information. It also creates an instance of the GitignoreChecker class to check files and folders against gitignore patterns.

The function uses a progress bar from the tqdm library to display the progress of checking files and folders that are not ignored. For each not_ignored_files in the progress bar, it checks if the file should be skipped based on the jump_files parameter. If the file ends with a specific substring, it is also skipped. Otherwise, it calls the generate_file_structure function to generate the file structure for the not_ignored_files.

If an error occurs during the generation of the file structure for a specific file, an error message is printed, and the process continues with the next file. The progress bar is updated to show the current file being processed.

Finally, the function returns the repo_structure dictionary containing the file structure information for all files in the repository.

The generate_overall_structure function is an essential part of the file handling process in the project. It is called by the init_meta_info function in the MetaInfo class to initialize the meta information for a repository. The generated file structure information is used for various purposes, such as generating documentation, updating JSON data, and converting content to markdown format.

**Note**:
- The jump_files parameter allows skipping specific files during the file structure generation process.
- The generate_overall_structure function relies on the generate_file_structure function to generate the file structure for each file.
- The function uses the tqdm library to display a progress bar during the file structure generation process.

**Output Example**:
{
    "file1.py": {
        "function1": {
            "type": "function",
            "start_line": 10,
            "end_line": 20,
            "parent": None
        },
        "class1": {
            "type": "class",
            "start_line": 5,
            "end_line": 25,
            "parent": None
        }
    },
    "file2.py": {
        "function2": {
            "type": "function",
            "start_line": 15,
            "end_line": 25,
            "parent": None
        },
        "class2": {
            "type": "class",
            "start_line": 8,
            "end_line": 30,
            "parent": None
        }
    },
    ...
}
***
### FunctionDef convert_to_markdown_file(self, file_path)
**convert_to_markdown_file**: The function of convert_to_markdown_file is to convert the content of a file to markdown format.

**parameters**:
- file_path (str, optional): The relative path of the file to be converted. If not provided, the default file path, which is None, will be used.

**Code Description**:
The `convert_to_markdown_file` function reads the project hierarchy JSON file to retrieve information about the specified file. It then processes the file's content and structure to generate markdown-formatted documentation. The function iterates through the objects in the file, organizes them based on their hierarchy level, and constructs markdown content accordingly. If the file object is not found in the project hierarchy JSON, a `ValueError` is raised.

In the project, this function is primarily called when processing file changes. When a file is detected to have changes, the `convert_to_markdown_file` function is invoked to update the markdown documentation for the file. If the file already exists in the project hierarchy, the function updates the existing markdown content. Otherwise, if the file is new, a new markdown document is generated for the file.

**Note**:
Ensure that the project hierarchy JSON file contains the necessary information about the file structure before calling this function.

**Output Example**:
```
# FunctionDef example_function():
This is an example function.
***
```
***
