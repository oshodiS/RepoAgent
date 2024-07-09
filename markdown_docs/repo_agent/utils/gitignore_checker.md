## ClassDef GitignoreChecker
**GitignoreChecker**: The function of GitignoreChecker is to check files and folders in a specified directory against patterns defined in a .gitignore file.

**attributes**:
- directory: The directory to be checked.
- gitignore_path: The path to the .gitignore file.
- folder_patterns: List of patterns for folders.
- file_patterns: List of patterns for files.

**Code Description**:
The GitignoreChecker class initializes with a directory and a .gitignore file path. It loads and parses the .gitignore file, splitting the patterns into folder and file patterns. The class provides methods to check files and folders in the directory against the gitignore patterns to determine which files are not ignored and have a '.py' extension. The check_files_and_folders method returns a list of paths to files that meet the criteria.

In the project, the GitignoreChecker is utilized in the FileHandler class to generate the overall structure of a repository. It checks files and folders in the repository against the gitignore patterns to exclude certain files from processing based on predefined conditions.

**Note**:
- Ensure the .gitignore file is correctly set up to define the exclusion patterns.
- The check_files_and_folders method specifically filters files with a '.py' extension that are not ignored by the gitignore patterns.

**Output Example**:
['src/main.py', 'utils/helper.py']
### FunctionDef __init__(self, directory, gitignore_path)
**__init__**: The function of __init__ is to initialize the GitignoreChecker with a specific directory and the path to a .gitignore file.

**parameters**:
- directory (str): The directory to be checked.
- gitignore_path (str): The path to the .gitignore file.

**Code Description**:
The __init__ function sets the directory and gitignore_path attributes based on the provided parameters. It then calls the _load_gitignore_patterns function to load and parse the .gitignore file, extracting folder and file patterns which are stored in the folder_patterns and file_patterns attributes respectively.

The _load_gitignore_patterns function reads the content of the specified .gitignore file or falls back to a default path if the file is not found. It then processes the patterns and categorizes them into folder and file patterns. This function is crucial for initializing the GitignoreChecker with the necessary patterns for checking directories and files against the .gitignore rules.

**Note**:
Ensure that the gitignore_path attribute points to a valid .gitignore file or provide a fallback path if the specified file is not found. This function is essential for setting up the GitignoreChecker object with the required parameters for checking directories and files.
***
### FunctionDef _load_gitignore_patterns(self)
**_load_gitignore_patterns**: The function of _load_gitignore_patterns is to load and parse the .gitignore file, then split the patterns into folder and file patterns. If the specified .gitignore file is not found, it falls back to the default path.

**parameters**:
- None

**Code Description**:
The _load_gitignore_patterns function reads the content of the .gitignore file specified by the gitignore_path attribute. If the file is not found, it falls back to the default .gitignore path. The function then calls the _parse_gitignore function to extract patterns from the content and further processes these patterns by calling _split_gitignore_patterns to categorize them into folder and file patterns. Finally, it returns a tuple containing two lists - one for folder patterns and one for file patterns.

This function is part of the GitignoreChecker class and is called during the initialization of the class to set the folder_patterns and file_patterns attributes based on the loaded .gitignore file.

**Note**:
Ensure that the gitignore_path attribute points to a valid .gitignore file or provide a fallback path if the specified file is not found.

**Output Example**:
(['folder_pattern1', 'folder_pattern2'], ['file_pattern1', 'file_pattern2'])
***
### FunctionDef _parse_gitignore(gitignore_content)
**_parse_gitignore**: The function of _parse_gitignore is to parse the content of a .gitignore file and extract patterns as a list.

**parameters**:
- gitignore_content (str): The content of the .gitignore file.

**Code Description**:
The _parse_gitignore function takes the content of a .gitignore file as input and processes it line by line. It strips each line, checks if it is not empty and does not start with '#', then appends it to a list of patterns. Finally, it returns the list of extracted patterns.

In the project, _parse_gitignore is called by the _load_gitignore_patterns method of the GitignoreChecker class. The _load_gitignore_patterns method is responsible for loading and parsing the .gitignore file, then splitting the patterns into folder and file patterns. If the specified .gitignore file is not found, it falls back to a default path and reads the content. After loading the content, it calls _parse_gitignore to extract patterns from the content, and further processes the patterns by calling _split_gitignore_patterns to separate folder and file patterns before returning them as a tuple.

**Note**:
Ensure that the input gitignore_content is a valid string containing the content of a .gitignore file.

**Output Example**:
['pattern1', 'pattern2', 'pattern3']
***
### FunctionDef _split_gitignore_patterns(gitignore_patterns)
**_split_gitignore_patterns**: The function of _split_gitignore_patterns is to split the .gitignore patterns into folder patterns and file patterns.

**parameters**:
- gitignore_patterns (list): A list of patterns from the .gitignore file.

**Code Description**:
The _split_gitignore_patterns function takes a list of patterns from a .gitignore file as input. It then iterates through each pattern and categorizes them into folder patterns or file patterns based on whether the pattern ends with a '/'. The function returns two lists, one containing folder patterns and the other containing file patterns.

In the project, this function is called by the _load_gitignore_patterns method in the GitignoreChecker class. The _load_gitignore_patterns method loads and parses the .gitignore file, then utilizes _split_gitignore_patterns to further process the patterns into folder and file patterns.

**Note**:
Developers can use this function to organize and categorize patterns from a .gitignore file into folder and file patterns for better management.

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
The _is_ignored function iterates through the patterns provided and checks if the given path matches any of the patterns. It returns True if a match is found, otherwise False. Additionally, if the path is a directory (is_dir=True), it considers patterns that end with '/' as directory patterns.

This function is called within the check_files_and_folders method of the GitignoreChecker class. In the check_files_and_folders method, _is_ignored is used to filter out directories and files based on the gitignore patterns provided. It ensures that only files with the '.py' extension that are not ignored are included in the final list of not_ignored_files.

**Note**:
Developers should ensure that the patterns provided are correctly formatted to match the paths effectively.

**Output Example**:
```python
['folder/file1.py', 'folder/subfolder/file2.py', ...]
```
***
### FunctionDef check_files_and_folders(self)
**check_files_and_folders**: The function of check_files_and_folders is to check all files and folders in the given directory against the split gitignore patterns and return a list of files that are not ignored and have the '.py' extension. The returned file paths are relative to the self.directory.

**parameters**:
- self: The instance of the class.
- No additional parameters.

**Code Description**:
The check_files_and_folders function iterates through all files and folders in the specified directory using os.walk. It filters out directories based on the folder patterns and files based on the file patterns provided. Only files with the '.py' extension that are not ignored are included in the final list of not_ignored_files. The paths returned are relative to the self.directory.

This function utilizes the _is_ignored method from the GitignoreChecker class to determine if a file or directory should be ignored based on the gitignore patterns. By leveraging this method, the function ensures that only relevant files are included in the output list.

**Note**:
Developers should ensure that the gitignore patterns are correctly defined to accurately filter out files and directories based on the specified criteria.

**Output Example**:
['folder/file1.py', 'folder/subfolder/file2.py', ...]
***
