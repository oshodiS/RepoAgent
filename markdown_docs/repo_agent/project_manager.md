## ClassDef ProjectManager
**ProjectManager**: The function of ProjectManager is to manage the project structure and build a path tree for references.

**attributes**:
- repo_path: The path to the repository.
- project: The jedi Project associated with the repository path.
- project_hierarchy: The path to the project hierarchy JSON file.

**Code Description**:
The ProjectManager class initializes with the repository path and project hierarchy. It provides methods to get the project structure by recursively walking through the directory tree and build a path tree for references. The `get_project_structure` method returns the project structure as a string by traversing the directory tree. The `build_path_tree` method constructs a tree structure for references and marks the specified object with a star symbol.

The `build_path_tree` method utilizes nested dictionaries to represent the path tree structure. It processes the paths of who references whom, references who, and the document item path to create a hierarchical tree. The final tree is converted to a string format for readability.

In the project, the ProjectManager class is instantiated in the Runner class's `__init__` method. It is used to manage the project, detect changes, and interact with the ChatEngine and MetaInfo classes. The ProjectManager plays a crucial role in handling project-related operations and maintaining the project's structure and references.

**Note**: Ensure the correct paths are provided for repository, project hierarchy, and document items to generate accurate path trees.

**Output Example**:
```
    project_folder
        subfolder1
            file1.py
            file2.py
        subfolder2
            file3.py
```
### FunctionDef __init__(self, repo_path, project_hierarchy)
**__init__**: The function of __init__ is to initialize the ProjectManager object with the provided repository path and project hierarchy.

**parameters**:
- repo_path: A string representing the path to the repository.
- project_hierarchy: A string specifying the project hierarchy within the repository.

**Code Description**:
In this function, the provided repo_path is assigned to the self.repo_path attribute. Subsequently, a new jedi Project object is created using the repo_path and assigned to the self.project attribute. Additionally, the project_hierarchy path is constructed by joining repo_path, project_hierarchy, and "project_hierarchy.json", and stored in the self.project_hierarchy attribute.

**Note**:
- Ensure that the repo_path and project_hierarchy parameters are valid paths before calling this function to avoid any errors during initialization.
***
### FunctionDef get_project_structure(self)
**get_project_structure**: The function of get_project_structure is to return the structure of the project by recursively walking through the directory tree.

**parameters**:
- No external parameters are required for this function.

**Code Description**:
The get_project_structure function defines an inner function walk_dir to recursively walk through the directory tree starting from the repo_path provided. It appends the directory names and Python files (.py) found in the project structure to a list called structure. The final project structure is then returned as a string where each directory and Python file is listed with appropriate indentation.

**Note**:
- This function only considers directories and Python files within the project structure.
- Hidden files and directories (those starting with ".") are ignored during the structure retrieval process.

**Output Example**:
```
project_folder
  subfolder1
    file1.py
    file2.py
  subfolder2
    subfolder2_1
      file3.py
```
#### FunctionDef walk_dir(root, prefix)
**walk_dir**: The function of walk_dir is to recursively traverse a directory structure, ignoring hidden files and directories, and appending the names of Python files to a list.

**parameters**:
· root: The root directory to start the traversal from.
· prefix: A string representing the current indentation level in the directory structure.

**Code Description**:
The walk_dir function takes two parameters: root, which is the starting directory for the traversal, and prefix, which is used for indentation in the directory structure. It appends the basename of the current directory to the 'structure' list. It then iterates over the sorted list of items in the current directory. If an item starts with a ".", indicating a hidden file or directory, it is skipped. For each item, the function checks if it is a directory or a Python file. If it is a directory, the function is recursively called with the new path and an updated prefix. If it is a Python file, it appends the file name to the 'structure' list with the updated prefix.

**Note**:
- This function is useful for generating a structured representation of a directory tree, especially when looking for specific file types like Python files.
- Ensure that the 'structure' list is defined before calling the walk_dir function to store the directory structure.
***
***
### FunctionDef build_path_tree(self, who_reference_me, reference_who, doc_item_path)
**build_path_tree**: The function of build_path_tree is to construct a tree structure based on the provided paths and return the tree as a string representation.

**parameters**:
- who_reference_me: List of paths referencing the current object.
- reference_who: List of paths referenced by the current object.
- doc_item_path: Path of the document item.

**Code Description**:
The build_path_tree function initializes a tree structure using defaultdict. It then iterates over the paths in who_reference_me and reference_who lists to build a tree structure. The function processes the doc_item_path by splitting it into parts, adding a symbol to the last part, and traversing the tree accordingly. Finally, it converts the tree structure into a string representation recursively.

**Note**:
Ensure that the paths provided are valid and correctly formatted.
The function relies on the os module, so ensure it is imported and accessible.
The function assumes a specific path structure for proper tree construction.

**Output Example**:
```
    repo_agent
        project_manager.py
            ProjectManager
                ✳️build_path_tree
```
#### FunctionDef tree
**tree**: The function of tree is to return a defaultdict initialized with the tree function.

**parameters**: 
- No parameters are required for this function.

**Code Description**:
The tree function returns a defaultdict initialized with the tree function itself. This creates a recursive structure where any missing keys will be automatically created and initialized with another defaultdict with the same behavior.

**Note**: 
- The use of this function is particularly useful for creating nested data structures without the need to manually initialize each level.
- It is important to note that this function relies on the defaultdict class from the collections module in Python.

**Output Example**: 
defaultdict(<function tree at 0x00000123456789>)
***
#### FunctionDef tree_to_string(tree, indent)
**tree_to_string**: The function of tree_to_string is to convert a nested dictionary representing a tree structure into a string with proper indentation.

**parameters**:
- tree: A nested dictionary representing a tree structure.
- indent: An integer representing the current level of indentation (default is 0).

**Code Description**:
The function iterates through the items of the input tree dictionary, sorts them, and appends each key to the string with the appropriate level of indentation. If the corresponding value of a key is another dictionary, the function recursively calls itself with the nested dictionary and increments the indentation level.

**Note**:
- The function assumes that the input tree is a nested dictionary.
- The indentation is set to 4 spaces per level.

**Output Example**:
```
root
    branch1
        leaf1
        leaf2
    branch2
        leaf3
```
***
***
