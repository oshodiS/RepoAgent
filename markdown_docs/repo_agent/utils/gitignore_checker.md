## ClassDef GitignoreChecker
**GitignoreChecker**: The function of GitignoreChecker is to check files and folders in a specified directory against the patterns defined in a .gitignore file, returning a list of files that are not ignored and have the '.py' extension.

**attributes**:
- directory: The directory to be checked.
- gitignore_path: The path to the .gitignore file.
- folder_patterns: A list of patterns for folders extracted from the .gitignore file.
- file_patterns: A list of patterns for files extracted from the .gitignore file.

**Code Description**:
The GitignoreChecker class initializes with a directory and a .gitignore file path. It loads and parses the .gitignore file, splitting the patterns into folder and file patterns. The class provides methods to check files and folders in the directory against the gitignore patterns and determine which files are not ignored and have the '.py' extension.

The `_load_gitignore_patterns` method reads the .gitignore file content, falling back to a default path if the specified file is not found. It then parses the content and splits the patterns into folder and file patterns using `_parse_gitignore` and `_split_gitignore_patterns` static methods.

The `_is_ignored` static method checks if a given path matches any of the patterns provided. The `check_files_and_folders` method walks through the directory, filtering out ignored files and folders based on the gitignore patterns, and returns a list of non-ignored '.py' files relative to the directory.

In the project, the `generate_overall_structure` method in the FileHandler class utilizes GitignoreChecker to check files and folders in a repository against gitignore patterns. It skips certain files based on conditions and generates the structure of the repository by calling `generate_file_structure` for each non-ignored file.

**Note**:
- Ensure the .gitignore file is correctly set up with the desired patterns for effective file filtering.
- The class focuses on checking files and folders against gitignore patterns and filtering out specific file types based on the '.py' extension.

**Output Example**:
['src/main.py', 'utils/helper.py', ...]
### FunctionDef __init__(self, directory, gitignore_path)
**__init__**: The function of __init__ is to initialize the GitignoreChecker with a specific directory and the path to a .gitignore file.

**Parameters**:
- directory (str): The directory to be checked.
- gitignore_path (str): The path to the .gitignore file.

**Code Description**:
The __init__ function sets the directory and gitignore_path attributes based on the provided parameters. It then calls the _load_gitignore_patterns function to load and parse the .gitignore file, extracting folder and file patterns. These patterns are stored in the folder_patterns and file_patterns attributes respectively.

The _load_gitignore_patterns function is responsible for reading the content of the specified .gitignore file or falling back to the default path if the file is not found. It then parses the content to extract patterns for folders and files, returning them as separate lists.

This initialization process ensures that the GitignoreChecker is properly configured with the necessary directory and .gitignore file path, along with the corresponding patterns for folders and files.

**Note**:
Ensure that the gitignore_path attribute is correctly set before calling the __init__ function to ensure proper initialization of the GitignoreChecker object.
***
### FunctionDef _load_gitignore_patterns(self)
**_load_gitignore_patterns**: The function of _load_gitignore_patterns is to load and parse the .gitignore file, then split the patterns into folder and file patterns. If the specified .gitignore file is not found, it falls back to the default path.

**Parameters**:
- None

**Code Description**:
The _load_gitignore_patterns function first attempts to open and read the content of the .gitignore file specified by the gitignore_path attribute. If the file is not found, it falls back to the default .gitignore path. The content of the file is then passed to the _parse_gitignore function to extract patterns. Finally, the extracted patterns are further processed by the _split_gitignore_patterns function to separate them into folder and file patterns. The function returns a tuple containing two lists - one for folder patterns and one for file patterns.

This function is called within the __init__ method of the GitignoreChecker class, where it is used to initialize the folder_patterns and file_patterns attributes based on the loaded .gitignore file.

**Note**:
Ensure that the gitignore_path attribute is correctly set before calling this function to load the .gitignore file.

**Output Example**:
(['folder_pattern1', 'folder_pattern2'], ['file_pattern1', 'file_pattern2'])
***
### FunctionDef _parse_gitignore(gitignore_content)
**_parse_gitignore**: The function of _parse_gitignore is to parse the .gitignore content and return patterns as a list.

**Parameters**:
- gitignore_content (str): The content of the .gitignore file.

**Code Description**:
The _parse_gitignore function takes the content of a .gitignore file as input and extracts patterns from it. It removes empty lines and lines starting with "#" from the content, returning the extracted patterns as a list.

This function is called by the _load_gitignore_patterns method in the GitignoreChecker class. In _load_gitignore_patterns, the .gitignore file is loaded, and its content is passed to _parse_gitignore for pattern extraction. The extracted patterns are then further processed in the _split_gitignore_patterns method.

**Note**:
Ensure that the input to _parse_gitignore is a valid .gitignore file content in string format.

**Output Example**:
['pattern1', 'pattern2', 'pattern3']
***
### FunctionDef _split_gitignore_patterns(gitignore_patterns)
**_split_gitignore_patterns**: The function of _split_gitignore_patterns is to split the .gitignore patterns into folder patterns and file patterns.

**parameters**:
- gitignore_patterns (list): A list of patterns from the .gitignore file.

**Code Description**:
The _split_gitignore_patterns function takes a list of patterns from a .gitignore file as input. It then iterates through each pattern and categorizes them into folder patterns or file patterns based on whether the pattern ends with a forward slash ("/"). Folder patterns are stored in the folder_patterns list, while file patterns are stored in the file_patterns list. The function returns a tuple containing two lists - one for folder patterns and one for file patterns.

This function is called by the _load_gitignore_patterns method in the GitignoreChecker class. In the _load_gitignore_patterns method, the .gitignore file is loaded and parsed, and the patterns are then passed to _split_gitignore_patterns to separate them into folder and file patterns.

**Note**:
Ensure that the input to _split_gitignore_patterns is a list of patterns from a .gitignore file for correct functionality.

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
The _is_ignored function iterates through the provided patterns to determine if the given path matches any of them. It also considers whether the path is a directory or not. If the path matches any pattern or if it is a directory and matches a specific pattern format, the function returns True. Otherwise, it returns False. This function is utilized to identify if a file or directory should be ignored based on the specified patterns.

In the project, _is_ignored is called within the check_files_and_folders method of the GitignoreChecker class. Within check_files_and_folders, _is_ignored is used to filter out directories and files based on the defined patterns. It helps in identifying files that are not ignored and have a '.py' extension, returning a list of such files relative to the specified directory.

**Note**:
Ensure that the patterns provided are correctly formatted to match the paths effectively.

**Output Example**:
['folder/file1.py', 'folder/subfolder/file2.py', ...]
***
### FunctionDef check_files_and_folders(self)
**check_files_and_folders**: The function of check_files_and_folders is to check all files and folders in the specified directory against split gitignore patterns. It returns a list of files that are not ignored and have the '.py' extension. The paths of the returned files are relative to the specified directory.

**parameters**:
- self: The instance of the class.
  
**Code Description**:
The check_files_and_folders function iterates through all files and folders in the given directory using os.walk. It filters out directories based on folder patterns and checks files against file patterns to identify those that are not ignored and have a '.py' extension. The function utilizes the _is_ignored method to determine if a file should be ignored based on the specified patterns. The final list contains paths to files that meet the criteria and are relative to the specified directory.

This function is called within the generate_overall_structure method of the FileHandler class in the project. It is used to obtain a list of files that are not ignored and have a '.py' extension, which are then processed to generate the overall structure of the repository. The function plays a crucial role in filtering out files that should be excluded based on the gitignore patterns.

**Note**:
Ensure that the directory, folder patterns, and file patterns are correctly set to obtain the desired list of files.

**Output Example**:
['folder/file1.py', 'folder/subfolder/file2.py', ...]
***
