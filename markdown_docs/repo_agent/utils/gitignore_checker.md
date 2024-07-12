## ClassDef GitignoreChecker
**GitignoreChecker**: The function of GitignoreChecker is to check files and folders in a specified directory against patterns defined in a .gitignore file and return a list of files that are not ignored and have the '.py' extension.

**attributes**:
- directory: The directory to be checked.
- gitignore_path: The path to the .gitignore file.
- folder_patterns: List of patterns for folders specified in the .gitignore file.
- file_patterns: List of patterns for files specified in the .gitignore file.

**Code Description**:
The GitignoreChecker class initializes with a directory and a path to a .gitignore file. It loads and parses the .gitignore file, splitting the patterns into folder and file patterns. The class provides methods to check files and folders in the directory against the split gitignore patterns to identify files that are not ignored and have the '.py' extension.

When called in the 'generate_overall_structure' method of the 'FileHandler' class, GitignoreChecker is used to filter out files based on the .gitignore rules. It ensures that certain files are not processed based on specific conditions defined in the calling code.

**Note**:
Developers can utilize GitignoreChecker to handle file and folder filtering based on .gitignore rules effectively.

**Output Example**:
['folder1/file1.py', 'folder2/file2.py', ...]
### FunctionDef __init__(self, directory, gitignore_path)
**__init__**: The function of __init__ is to initialize the GitignoreChecker with a specific directory and the path to a .gitignore file.

**parameters**:
- directory (str): The directory to be checked.
- gitignore_path (str): The path to the .gitignore file.

**Code Description**:
The __init__ function sets the directory and gitignore path based on the provided parameters. It then calls the _load_gitignore_patterns function to load and parse the .gitignore file, extracting folder and file patterns for further use. This function serves as the constructor for the GitignoreChecker class, preparing it for gitignore pattern checking operations.

**Note**:
Developers should ensure that the directory and gitignore path are correctly specified to enable proper initialization of the GitignoreChecker object.
***
### FunctionDef _load_gitignore_patterns(self)
**_load_gitignore_patterns**: The function of _load_gitignore_patterns is to load and parse the .gitignore file, then split the patterns into folder and file patterns. If the specified .gitignore file is not found, it falls back to the default path.

**parameters**:
- No external parameters.

**Code Description**:
The _load_gitignore_patterns function attempts to open and read the content of a specified .gitignore file. In case the file is not found, it switches to a default path to read the content. The function then calls the _parse_gitignore function to extract patterns from the content and subsequently invokes the _split_gitignore_patterns function to categorize the patterns into folder and file patterns. This function encapsulates the process of loading, parsing, and splitting .gitignore patterns for further use.

This function is called within the __init__ method of the GitignoreChecker class to initialize the directory and gitignore path, and retrieve the folder and file patterns for the specified directory.

**Note**:
Developers utilizing this function should ensure that the .gitignore file is correctly formatted to avoid unexpected behavior.

**Output Example**:
(['folder_pattern1', 'folder_pattern2'], ['file_pattern1', 'file_pattern2'])
***
### FunctionDef _parse_gitignore(gitignore_content)
**_parse_gitignore**: The function of _parse_gitignore is to parse the content of a .gitignore file and extract patterns as a list.

**parameters**:
- gitignore_content (str): The content of the .gitignore file.

**Code Description**:
The _parse_gitignore function takes the content of a .gitignore file as input, processes each line to extract patterns that are not comments or empty lines, and returns a list of these patterns.

In the calling object _load_gitignore_patterns, the function first attempts to load the content of a specified .gitignore file. If the file is not found, it falls back to a default path. The function then calls _parse_gitignore to extract patterns from the content and further processes these patterns.

**Note**:
Developers can use this function to extract patterns from a .gitignore file for use in filtering files and directories in version control systems.

**Output Example**:
['pattern1', 'pattern2', 'pattern3']
***
### FunctionDef _split_gitignore_patterns(gitignore_patterns)
**_split_gitignore_patterns**: The function of _split_gitignore_patterns is to split the .gitignore patterns into folder patterns and file patterns.

**Parameters**:
- gitignore_patterns (list): A list of patterns from the .gitignore file.

**Code Description**:
The _split_gitignore_patterns function takes a list of .gitignore patterns as input and separates them into two lists based on whether they represent folder patterns or file patterns. It iterates through each pattern in the input list and categorizes them accordingly. Patterns ending with "/" are considered folder patterns, while others are treated as file patterns. The function then returns two lists, one containing folder patterns and the other containing file patterns.

This function is called by the _load_gitignore_patterns method in the GitignoreChecker class. In the _load_gitignore_patterns method, the .gitignore file is loaded and parsed, and the resulting patterns are passed to _split_gitignore_patterns for further processing. This division of responsibilities allows for a clear separation of concerns, with _split_gitignore_patterns handling the specific task of splitting patterns.

**Note**:
Developers using this function should ensure that the input list of gitignore patterns is correctly formatted to avoid any unexpected behavior.

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
The _is_ignored function iterates through the provided patterns to determine if the given path matches any of them. It also considers whether the path is a directory or not. If the path matches any pattern or if it is a directory and matches a specific pattern format, the function returns True. Otherwise, it returns False. 

This function is utilized within the check_files_and_folders method of the GitignoreChecker class. In the check_files_and_folders method, _is_ignored is used to filter out directories based on folder patterns and to identify files that are not ignored and have a '.py' extension. The function plays a crucial role in determining which files to include in the final list of not ignored Python files.

**Note**:
Developers should ensure that the path and patterns provided are in the correct format for accurate pattern matching.

**Output Example**:
False
***
### FunctionDef check_files_and_folders(self)
**check_files_and_folders**: The function of check_files_and_folders is to check all files and folders in the given directory against the split gitignore patterns and return a list of files that are not ignored and have the '.py' extension. The returned file paths are relative to the self.directory.

**parameters**:
- self: The instance of the class.
  
**Code Description**:
The check_files_and_folders function iterates through all files and folders in the specified directory, filtering out directories based on folder patterns and identifying files that are not ignored and have a '.py' extension. It utilizes the _is_ignored function to determine if a file should be included in the final list of not ignored Python files. The function returns a list of paths to files that meet the specified criteria.

This function is called within the generate_overall_structure method of the FileHandler class. In the generate_overall_structure method, check_files_and_folders is used to retrieve a list of not ignored files with the '.py' extension from the target repository. The function plays a crucial role in generating the overall structure of the repository by including relevant Python files.

**Note**:
Developers should ensure that the directory provided is valid and contains the necessary files for accurate processing.

**Output Example**:
['src/main.py', 'utils/helper.py', ...]
***
