## ClassDef ChangeDetector
**ChangeDetector**: The ChangeDetector class is responsible for handling file differences and change detection. It utilizes the FileHandler class to access the file system. The core functionality of the ChangeDetector class is to identify the changes in files since the last commit.

**Attributes**:
- repo_path (str): The path to the repository.
- repo (git.Repo): The Git repository object.

**Code Description**:
The ChangeDetector class provides several methods to track and analyze file changes in a Git repository.

The `__init__` method initializes a ChangeDetector object by setting the repository path and creating a Git repository object using the `git.Repo` class.

The `get_staged_pys` method retrieves the added Python files in the repository that have been staged. It uses the GitPython library to compare the staging area (index) with the original HEAD commit. The method returns a dictionary of changed Python files, where the keys are the file paths and the values are booleans indicating whether the file is newly created or not.

The `get_file_diff` method retrieves the changes made to a specific file. For new files, it adds them to the staging area and then gets the diff from the staging area. For non-new files, it gets the diff from HEAD. The method returns a list of changes made to the file.

The `parse_diffs` method parses the difference content obtained from the `get_file_diff` method. It extracts the added and deleted object information, which can be a class or a function. The method returns a dictionary containing the added and deleted line information.

The `identify_changes_in_structure` method identifies the structure of the function or class where changes have occurred. It traverses all changed lines and checks whether each line is within the start and end lines of a structure. If a line is within a structure, the structure is considered to have changed, and its name and the name of the parent structure are added to the corresponding set in the result dictionary. The method returns a dictionary containing the structures where changes have occurred.

The `get_to_be_staged_files` method retrieves all unstaged files in the repository that meet certain conditions. It checks whether the file extension changed to .md corresponds to a file that is already staged or if the file's path is the same as the 'project_hierarchy' field in the CONFIG. The method returns a list of the paths of these files.

The `add_unstaged_files` method adds the unstaged files that meet the conditions to the staging area.

**Note**: The `identify_changes_in_structure` method may have some issues and requires further testing and improvement. The `get_to_be_staged_files` method may also have some issues and could be implemented in a better way.

**Output Example**:
{
    'added': [
        (86, '    '),
        (87, '    def to_json_new(self, comments = True):'),
        (88, '        data = {'),
        (89, '            "name": self.node_name,'),
        ...
        (95, '')
    ],
    'removed': []
}
### FunctionDef __init__(self, repo_path)
**__init__**: The function of __init__ is to initialize a ChangeDetector object.

**parameters**:
- repo_path: A string representing the path to the repository.

**Code Description**:
The __init__ function initializes a ChangeDetector object by setting the repo_path attribute to the provided repo_path parameter. Additionally, it creates a git Repo object using the repo_path.

**Note**:
- Make sure to provide a valid repo_path string when initializing a ChangeDetector object.
***
### FunctionDef get_staged_pys(self)
**get_staged_pys**: The function of get_staged_pys is to retrieve added Python files in the repository that have been staged, indicating whether they are newly created or not.

**parameters**: 
- None

**Code Description**: 
The get_staged_pys function utilizes GitPython to detect staged changes in the repository. It compares the current staging area with the original HEAD commit to identify newly added Python files. The function then creates a dictionary where the keys represent file paths and the values indicate if the file is newly created.

When called, the function first retrieves the repository object. It then detects staged changes by comparing the staging area with the HEAD commit, considering the reverse logic to correctly identify new files. Subsequently, it iterates through the detected changes, filtering out Python files and determining if they are newly added based on the change type. Finally, it returns a dictionary containing the paths of changed Python files along with a boolean value indicating if they are newly created.

This function is crucial for tracking staged changes specifically for Python files in a Git repository.

**Note**: 
- The function relies on the GitPython library to interact with Git repositories.
- Understanding the logic behind the GitPython library's comparison mechanism is essential for interpreting the results accurately.

**Output Example**: 
{
    'path/to/file1.py': True,
    'path/to/file2.py': False,
    ...
}
***
### FunctionDef get_file_diff(self, file_path, is_new_file)
**get_file_diff**: The function of get_file_diff is to retrieve the changes made to a specific file. For new files, it uses git diff --staged to get the differences.

**parameters**:
- file_path (str): The relative path of the file.
- is_new_file (bool): Indicates whether the file is a new file.

**Code Description**:
The get_file_diff function first determines if the file is new or not based on the is_new_file parameter. If the file is new, it adds the file to the staging area using git add command and then retrieves the differences using git diff --staged. If the file is not new, it retrieves the differences from HEAD using git diff. The function returns a list of changes made to the file.

In the project, the get_file_diff function is called within the process_file_changes method of the Runner class. It is used to parse the differences in the file and identify changes in the file structure. The identified changes are then used to update the project_hierarchy.json file and generate corresponding Markdown documentation for the file.

**Note**:
- Ensure that the Git command-line tool is installed and accessible in the environment where this function is used.
- Handle the returned list of changes appropriately based on the requirements of the project.

**Output Example**:
['- line 1: old content', '+ line 1: new content', '...']
***
### FunctionDef parse_diffs(self, diffs)
**parse_diffs**: The function of parse_diffs is to parse the difference content from a list of differences, extract added and deleted object information (classes or functions), and return a dictionary containing added and deleted line information.

**parameters**:
- diffs (list): A list containing difference content obtained by the get_file_diff() function inside the class.

**Code Description**:
The parse_diffs function processes the differences in the content by iterating through the provided list of differences. It extracts added and deleted object information by analyzing the lines starting with "+" or "-", and updates the line numbers accordingly. The function then returns a dictionary containing the added and removed line information.

In the project, the parse_diffs function is called within the process_file_changes method of the Runner class. It is used to identify changes in the structure of Python files by parsing the differences and extracting added and removed objects. The identified changes are further processed to update the project's JSON structure information, convert the changes to markdown content, and write the markdown content to a .md file.

**Note**: 
- The parse_diffs function is essential for detecting changes in Python files and updating project documentation.
- The function relies on the get_file_diff() method to obtain the list of differences for processing.

**Output Example**:
{'added': [(86, '    '), (87, '    def to_json_new(self, comments = True):'), (88, '        data = {'), (89, '            "name": self.node_name,')...(95, '')], 'removed': []}
***
### FunctionDef identify_changes_in_structure(self, changed_lines, structures)
**identify_changes_in_structure**: The function of identify_changes_in_structure is to identify the structures (functions or classes) where changes have occurred based on the provided changed lines and structures list.

**parameters**:
- changed_lines (dict): A dictionary containing the line numbers where changes have occurred, with keys 'added' and 'removed'.
- structures (list): A list of function or class structures, each containing structure type, name, start line number, end line number, and parent structure name.

**Code Description**:
The function iterates through the changed lines and structures to determine if a line falls within a structure's start and end lines. If a line is within a structure, the function adds the structure's name and parent structure's name to the result dictionary based on whether the line was added or removed.

The function returns a dictionary with keys 'added' and 'removed', each containing a set of structure names and parent structure names where changes have occurred.

This function is called within the `process_file_changes` method in the `Runner` class. It is used to identify changes in the structures of Python files and update the project hierarchy accordingly. The identified changes are logged, and if the corresponding file is found in the project hierarchy, its JSON structure information is updated and written back to the file. Additionally, the function converts the changed JSON content to Markdown format and updates the Markdown file. If the file is not found in the project hierarchy, a new item is added. Finally, the function adds the updated Markdown files to the staging area in the Git repository.

**Note**: Ensure that the `changed_lines` and `structures` parameters are correctly formatted to match the expected input structure.

**Output Example**: 
{'added': {('PipelineAutoMatNode', None), ('to_json_new', 'PipelineAutoMatNode')}, 'removed': set()}
***
### FunctionDef get_to_be_staged_files(self)
**get_to_be_staged_files**: The function of get_to_be_staged_files is to retrieve all unstaged files in the repository that meet specific conditions and return a list of their paths.

**parameters**:
- None

**Code Description**:
The `get_to_be_staged_files` function first retrieves the already staged files in the repository. It then checks for unstaged files that meet the conditions of either having a corresponding staged file when the extension is changed to .md or having a path matching the 'project_hierarchy' field in the configuration. The function processes untracked files and unstaged files, adding them to the list of files to be staged if they meet the specified conditions. Finally, it returns a list of relative file paths to the repository that are either modified but not staged or untracked and meet the conditions mentioned above.

This function is called by the `add_unstaged_files` method in the `ChangeDetector` class. The `add_unstaged_files` method utilizes the `get_to_be_staged_files` function to identify unstaged files meeting the conditions and adds them to the staging area using Git commands.

**Note**:
- The function handles both untracked and unstaged files based on specific conditions.
- It interacts with Git to add identified files to the staging area.

**Output Example**:
['path/to/unstaged_file1.py', 'path/to/unstaged_file2.md', ...]
***
### FunctionDef add_unstaged_files(self)
**add_unstaged_files**: The function of add_unstaged_files is to add unstaged files that meet specific conditions to the staging area of a Git repository.

**parameters**:
- None

**Code Description**:
The `add_unstaged_files` function is a method of the `ChangeDetector` class in the `change_detector.py` file. It is responsible for identifying unstaged files in the repository that meet certain conditions and adding them to the staging area using Git commands.

The function first calls the `get_to_be_staged_files` method to retrieve a list of unstaged files that meet the conditions. It then iterates over each file path in the list and constructs a Git command to add the file to the staging area. The command is executed using the `subprocess.run` function with the `shell=True` and `check=True` parameters, ensuring that the command is executed in the shell and any errors are raised as exceptions.

Finally, the function returns the list of unstaged files that were successfully added to the staging area.

This function is called by the `run` method in the `Runner` class in the `runner.py` file. The `run` method is responsible for running the document update process, and it utilizes the `add_unstaged_files` method to add unstaged files to the staging area after generating and updating the documents.

**Note**:
- The function interacts with Git to add unstaged files to the staging area.
- It relies on the `get_to_be_staged_files` method to identify unstaged files that meet the specified conditions.

**Output Example**:
['path/to/unstaged_file1.py', 'path/to/unstaged_file2.md', ...]
***
