## ClassDef ChangeDetector
**ChangeDetector**: The ChangeDetector class is responsible for handling file differences and change detection. It utilizes the FileHandler class to access the file system. The core functionality of the ChangeDetector class is to identify changes in files since the last commit.

**Attributes**:
- repo_path (str): The path to the repository.
- repo (git.Repo): The Git repository object.

**Code Description**:
The ChangeDetector class provides several methods to track and analyze changes in files within a Git repository.

The `__init__` method initializes a ChangeDetector object by setting the repo_path attribute and creating a git.Repo object for the specified repository path.

The `get_staged_pys` method retrieves the added Python files in the repository that have been staged. It uses the GitPython library to compare the staging area (index) with the original HEAD commit. The method returns a dictionary of changed Python files, where the keys are the file paths and the values are booleans indicating whether the file is newly created or not.

The `get_file_diff` method retrieves the changes made to a specific file. For new files, it adds them to the staging area and then gets the diff from the staging area. For non-new files, it gets the diff from HEAD. The method returns a list of changes made to the file.

The `parse_diffs` method parses the difference content obtained from the `get_file_diff` method. It extracts the added and deleted object information, which can be a class or a function. The method returns a dictionary containing the added and deleted line information.

The `identify_changes_in_structure` method identifies the structure (function or class) where changes have occurred. It traverses all changed lines and checks whether each line falls within the start and end line numbers of a structure. If a line is within a structure, the structure is considered to have changed, and its name and the name of the parent structure are added to the corresponding set in the result dictionary. The method returns a dictionary containing the structures where changes have occurred.

The `get_to_be_staged_files` method retrieves all unstaged files in the repository that meet certain conditions. It checks for files with extensions changed to .md that correspond to already staged files, as well as files with paths matching the 'project_hierarchy' field in the CONFIG. The method returns a list of the paths of these files.

The `add_unstaged_files` method adds unstaged files that meet the conditions to the staging area. It calls the `get_to_be_staged_files` method to retrieve the files and uses the git add command to add them to the staging area.

**Note**: The `identify_changes_in_structure` method may have some issues and requires further testing and improvement. The `get_to_be_staged_files` method may also have some issues and may benefit from better implementation.

**Output Example**: 
{
    'added': [
        (86, '    '),
        (87, '    def to_json_new(self, comments = True):'),
        (88, '        data = {'),
        (89, '            "name": self.node_name,'),
        ...
    ],
    'removed': []
}
### FunctionDef __init__(self, repo_path)
**__init__**: The function of __init__ is to initialize a ChangeDetector object.

**parameters**:
- repo_path: A string representing the path to the repository.

**Code Description**:
The __init__ function initializes a ChangeDetector object by assigning the provided repo_path to the self.repo_path attribute. Additionally, it creates a git Repo object using the repo_path.

**Note**:
- Make sure to provide a valid repo_path string when initializing the ChangeDetector object to ensure proper functionality.
***
### FunctionDef get_staged_pys(self)
**get_staged_pys**: The function of get_staged_pys is to retrieve added Python files in the repository that have been staged.

**parameters**: 
- No external parameters are required for this function.

**Code Description**: 
The get_staged_pys function operates by first obtaining the repository object. It then detects staged changes by utilizing the GitPython library to compare the staging area with the original HEAD commit. By iterating through the detected differences, the function identifies added or modified Python files that end with the ".py" extension. The function constructs a dictionary where the keys represent the file paths, and the values indicate whether the file is newly created or not based on the change type.

In the project, this function is called within the TestChangeDetector class to test the functionality of identifying staged Python files. The test scenario involves creating a new Python file, staging it, initializing a ChangeDetector object with the repository path, and then verifying that the newly created file is present in the list of staged files.

**Note**: 
It is crucial to note that the logic of the GitPython library differs from the standard Git behavior, particularly in handling new files in the staging area. The use of the R=True parameter is essential to ensure correct comparison and identification of newly added files.

**Output Example**: 
{
    'new_test_file.py': True
}
***
### FunctionDef get_file_diff(self, file_path, is_new_file)
**get_file_diff**: The function of get_file_diff is to retrieve the changes made to a specific file. For new files, it uses git diff --staged to get the differences.

**parameters**:
- file_path (str): The relative path of the file.
- is_new_file (bool): Indicates whether the file is a new file.

**Code Description**:
The `get_file_diff` function retrieves the changes made to a file based on the provided file path and whether the file is new or not. If the file is new, it adds the file to the staging area using Git commands and then retrieves the differences using git diff --staged. For existing files, it gets the differences from the HEAD. The function returns a list of changes made to the file.

This function is called within the `process_file_changes` method in the `Runner` class. In the `process_file_changes` method, the `get_file_diff` function is used to obtain the changes in the file specified by the `file_path` parameter. The changes are then further processed to identify the changes in the file structure and update the project hierarchy accordingly.

**Note**:
Ensure that the `repo` attribute is properly initialized before calling this function to avoid errors.
Make sure to handle exceptions related to subprocess calls appropriately.

**Output Example**:
['- line 1: old content', '+ line 1: new content']
***
### FunctionDef parse_diffs(self, diffs)
**parse_diffs**: The function of parse_diffs is to parse the difference content from a list of differences, extract added and deleted object information, and return a dictionary containing added and deleted line information.

**parameters**:
- diffs (list): A list containing difference content obtained from the get_file_diff() function inside the class.

**Code Description**:
The parse_diffs function processes the differences in the provided list, identifies added and removed lines, and constructs a dictionary with information about the changes. It iterates through the differences, extracts line numbers, and categorizes lines as added or removed based on specific prefixes. The function then returns a dictionary containing the added and removed line information.

When called within the project, the parse_diffs function is utilized in the process_file_changes method of the Runner class. In this context, parse_diffs is used to identify changes in structure within Python files, update corresponding JSON files, convert content to Markdown, and manage version control operations.

**Note**: 
- The parse_diffs function is dependent on the get_file_diff() method to obtain the difference content.
- The function distinguishes between added and removed lines based on specific prefixes in the differences.
- It is crucial to ensure the correct input format (list of differences) when calling the parse_diffs function.

**Output Example**:
{'added': [(86, '    '), (87, '    def to_json_new(self, comments = True):'), (88, '        data = {'), (89, '            "name": self.node_name,')...(95, '')], 'removed': []}
***
### FunctionDef identify_changes_in_structure(self, changed_lines, structures)
**identify_changes_in_structure**: The function of identify_changes_in_structure is to identify the structures (functions or classes) where changes have occurred based on the provided changed lines and structures list.

**parameters**:
- changed_lines (dict): A dictionary containing the line numbers where changes have occurred, with keys 'added' and 'removed'.
- structures (list): A list of function or class structures containing structure type, name, start line number, end line number, and parent structure name.

**Code Description**:
The function iterates through the changed lines and structures to determine if a line falls within a structure's start and end lines. If a line is within a structure, the function adds the structure's name and parent structure's name to the result dictionary based on whether the line was added or removed.

In the calling object `process_file_changes` in `runner.py`, this function is used to identify changes in the structure of a file by parsing the differences in the file, extracting functions and classes, and updating the project hierarchy information accordingly. The identified changes are logged, and if the file is found in the project hierarchy, its information is updated and written back to the JSON file. Additionally, a Markdown file is created based on the updated information. If the file is not found, a new item is added to the project hierarchy.

**Note**: 
- Ensure that the `changed_lines` and `structures` parameters are correctly formatted as described in the function documentation.
- The function assumes that the structures list is obtained from `get_functions_and_classes` method.
- The output dictionary contains sets of structure names and parent structure names for added and removed changes.

**Output Example**: 
{'added': {('PipelineAutoMatNode', None), ('to_json_new', 'PipelineAutoMatNode')}, 'removed': set()}
***
### FunctionDef get_to_be_staged_files(self)
**get_to_be_staged_files**: The function of get_to_be_staged_files is to retrieve all unstaged files in the repository that meet specific conditions and return a list of their paths.

**parameters**:
- None

**Code Description**:
The `get_to_be_staged_files` function first retrieves the already staged files in the repository. It then identifies unstaged files based on two conditions: files whose extension changes to `.md` correspond to staged files, and files whose path matches the 'project_hierarchy' field in the configuration. The function processes untracked files and unstaged files separately, checking if they meet the specified conditions for inclusion in the list of files to be staged. Finally, it returns a list of relative file paths that are either modified but not staged or untracked and meet the defined conditions.

In the project, this function is called by the `add_unstaged_files` method in the `ChangeDetector` class. The `add_unstaged_files` method utilizes the `get_to_be_staged_files` function to identify unstaged files meeting the conditions and adds them to the staging area using Git commands.

**Note**:
- The function handles both untracked and unstaged files based on specific conditions to determine which files should be staged.
- It interacts with the Git repository to identify staged and unstaged files accurately.

**Output Example**:
['path/to/unstaged_file1.md', 'path/to/unstaged_file2.py', ...]
***
### FunctionDef add_unstaged_files(self)
**add_unstaged_files**: The function of add_unstaged_files is to add unstaged files that meet specific conditions to the staging area in a Git repository.

**parameters**:
- None

**Code Description**:
The `add_unstaged_files` function is a method of the `ChangeDetector` class in the `repo_agent/change_detector.py` file. It is responsible for adding unstaged files to the staging area in a Git repository. 

The function first calls the `get_to_be_staged_files` method to retrieve a list of unstaged files that meet certain conditions. It then iterates over each file path in the list and constructs a Git command to add the file to the staging area. The `subprocess.run` function is used to execute the Git command.

Finally, the function returns the list of unstaged files that were added to the staging area.

This function is called within the `run` method of the `Runner` class in the `repo_agent/runner.py` file. The `run` method is responsible for running the document update process. After generating and updating the documents, the `add_unstaged_files` method is called to add the newly generated Markdown files to the staging area.

**Note**:
- The function relies on the `get_to_be_staged_files` method to retrieve the list of unstaged files that meet the conditions.
- It uses the `subprocess.run` function to execute Git commands for adding files to the staging area.

**Output Example**:
['path/to/unstaged_file1.md', 'path/to/unstaged_file2.py', ...]
***
