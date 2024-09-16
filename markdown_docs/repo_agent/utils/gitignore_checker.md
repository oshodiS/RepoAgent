## ClassDef GitignoreChecker
**GitignoreChecker**: The function of GitignoreChecker is to check files and folders in a specified directory against patterns defined in a .gitignore file.

**attributes**:
- directory: The directory to be checked.
- gitignore_path: The path to the .gitignore file.
- folder_patterns: List of patterns for folders.
- file_patterns: List of patterns for files.

**Code Description**:
The GitignoreChecker class provides functionality to initialize with a directory and a .gitignore file path. It loads and parses the .gitignore file, splitting the patterns into folder and file patterns. The class also includes methods to check if a path is ignored based on the defined patterns and to check files and folders in the directory against the split gitignore patterns to return a list of files that are not ignored and have the '.py' extension.

In the project, the GitignoreChecker is utilized in the FileHandler class to generate the overall structure of a repository. It checks files and folders in the repository against the gitignore patterns to exclude certain files from processing.

**Note**:
- Ensure that the .gitignore file is correctly set up to define the patterns for ignoring files and folders.
- Make sure to provide the correct directory and .gitignore file path when initializing the GitignoreChecker.

**Output Example**:
['src/main.py', 'utils/helper.py']
### FunctionDef __init__(self, directory, gitignore_path)
**__init__**: The function of __init__ is to initialize the GitignoreChecker with a specific directory and the path to a .gitignore file.

**parameters**:
- directory (str): The directory to be checked.
- gitignore_path (str): The path to the .gitignore file.

**Code Description**:
The __init__ function sets the directory and gitignore_path attributes based on the provided parameters. It then calls the _load_gitignore_patterns function to load and parse the .gitignore file, extracting folder and file patterns which are stored in the folder_patterns and file_patterns attributes respectively. This function serves as the constructor for the GitignoreChecker class, preparing the necessary data for checking against the .gitignore file.

**Note**:
Developers can utilize this function to instantiate the GitignoreChecker class with the required directory and .gitignore file path, enabling efficient checking against the specified patterns.
***
### FunctionDef _load_gitignore_patterns(self)
**_load_gitignore_patterns**: The function of _load_gitignore_patterns is to load and parse the .gitignore file, then split the patterns into folder and file patterns. If the specified .gitignore file is not found, it falls back to the default path.

**parameters**:
- No external parameters are required explicitly.

**Code Description**:
The _load_gitignore_patterns function attempts to open and read the content of the .gitignore file specified by the gitignore_path attribute. If the file is not found, it falls back to the default .gitignore path. Once the content is obtained, the function calls the _parse_gitignore function to extract patterns from the content. Subsequently, it utilizes the _split_gitignore_patterns function to categorize the patterns into folder and file patterns. Finally, it returns a tuple containing two lists - one for folder patterns and one for file patterns.

This function is an integral part of the GitignoreChecker class and plays a crucial role in processing .gitignore file patterns efficiently. It relies on the _parse_gitignore function to extract patterns and the _split_gitignore_patterns function to organize the patterns into distinct categories. The extracted patterns can be used for various purposes such as filtering files or directories based on the specified patterns.

**Note**:
Developers can leverage this function to handle .gitignore file patterns effectively within their projects.

**Output Example**:
(['folder_pattern1', 'folder_pattern2'], ['file_pattern1', 'file_pattern2'])
***
### FunctionDef _parse_gitignore(gitignore_content)
**_parse_gitignore**: The function of _parse_gitignore is to parse the content of a .gitignore file and extract patterns as a list.

**parameters**:
- gitignore_content (str): The content of the .gitignore file.

**Code Description**:
The _parse_gitignore function takes the content of a .gitignore file as input, processes each line, and extracts non-empty lines that do not start with a '#' character as patterns. These patterns are then returned as a list.

In the project, this function is called by the _load_gitignore_patterns method in the GitignoreChecker class. The _load_gitignore_patterns method loads and reads the .gitignore file, then utilizes _parse_gitignore to extract patterns from the content. The extracted patterns are further processed and split into folder and file patterns before being returned as a tuple.

**Note**:
Developers can use this function to extract patterns from .gitignore files efficiently for various purposes such as filtering files or directories based on the specified patterns.

**Output Example**:
['pattern1', 'pattern2', 'pattern3']
***
### FunctionDef _split_gitignore_patterns(gitignore_patterns)
**_split_gitignore_patterns**: The function of _split_gitignore_patterns is to split the .gitignore patterns into folder patterns and file patterns.

**parameters**:
- gitignore_patterns (list): A list of patterns from the .gitignore file.

**Code Description**:
The _split_gitignore_patterns function takes a list of patterns from a .gitignore file as input. It then iterates through each pattern and categorizes them into folder patterns or file patterns based on whether the pattern ends with a '/'. The function returns two lists, one containing folder patterns and the other containing file patterns.

In the project, this function is called by the _load_gitignore_patterns method in the GitignoreChecker class. The _load_gitignore_patterns method reads and parses the .gitignore file content and then utilizes _split_gitignore_patterns to separate the patterns into folder and file patterns.

**Note**:
Developers can use this function to organize and categorize patterns from a .gitignore file efficiently.

**Output Example**:
(folder_patterns, file_patterns)
***
### FunctionDef _is_ignored(path, patterns, is_dir)
**_is_ignored**: The function of _is_ignored is to check if the given path matches any of the patterns.

**parameters**:
- path (str): The path to check.
- patterns (list): A list of patterns to check against.
- is_dir (bool): True if the path is a directory, False otherwise.

**Code Description**:
The _is_ignored function iterates through the patterns provided. It uses fnmatch to check if the path matches any pattern. If the path is a directory, it also considers patterns ending with "/" to match directories. The function returns True if the path matches any pattern, otherwise False. 

This function is utilized within the check_files_and_folders method of the GitignoreChecker class. In the check_files_and_folders method, _is_ignored is used to filter out directories based on folder patterns and to identify files that are not ignored and have a '.py' extension. The function plays a crucial role in determining which files to include in the final list of not ignored Python files.

**Note**:
Developers should ensure that the patterns provided are correctly formatted to match the paths effectively.

**Output Example**:
```python
["folder/file.py", "folder2/script.py"]
```
***
### FunctionDef check_files_and_folders(self)
**check_files_and_folders**: The function of check_files_and_folders is to check all files and folders in the given directory against the split gitignore patterns and return a list of files that are not ignored and have the '.py' extension. The returned file paths are relative to the self.directory.

**parameters**:
- self: The instance of the class.
- No additional parameters.

**Code Description**:
The check_files_and_folders function iterates through all files and folders in the specified directory using os.walk. It filters out directories based on folder patterns and identifies files that are not ignored and have a '.py' extension. The function utilizes the _is_ignored method to determine if a file should be included in the final list of not ignored Python files. The paths of the non-ignored Python files are returned as a list relative to the specified directory.

The _is_ignored method is crucial in this function as it checks if a given path matches any of the provided patterns. By utilizing _is_ignored, check_files_and_folders can accurately filter out files and directories based on the gitignore patterns.

**Note**:
Developers should ensure that the gitignore patterns are correctly formatted to effectively match the paths and directories.

**Output Example**:
```python
["folder/file.py", "folder2/script.py"]
```
***
