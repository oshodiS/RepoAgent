## ClassDef ProjectManager
**ProjectManager**: The function of ProjectManager is to manage the project structure and build a path tree for references.

**attributes**:
- repo_path: The path to the repository.
- project: The jedi Project associated with the repository path.
- project_hierarchy: The path to the project hierarchy JSON file.

**Code Description**:
The ProjectManager class initializes with the repository path and project hierarchy. It provides two main functions:

1. **get_project_structure**: This method recursively walks through the directory tree of the project and returns the project structure as a string.

2. **build_path_tree**: This method builds a tree structure based on the references between different paths in the project. It takes three parameters - who_reference_me, reference_who, and doc_item_path. It constructs trees for who_reference_me and reference_who paths and adds a star (*) before the last object in doc_item_path to signify the main object. The method then converts the tree structure to a string representation.

The ProjectManager class is utilized in the runner module to manage the project, detect changes, and interact with the chat engine. It is responsible for initializing the project, creating fake files if the project hierarchy does not exist, loading meta information, and updating the project hierarchy with new information.

**Note**: Ensure the proper setup of the repository path and project hierarchy to utilize the ProjectManager effectively.

**Output Example**:
```
    project_folder
        subfolder1
            file1.py
            file2.py
        subfolder2
            file3.py
    ...
```
### FunctionDef __init__(self, repo_path, project_hierarchy)
**__init__**: The function of __init__ is to initialize the ProjectManager object with the provided repository path and project hierarchy.

**parameters**:
- repo_path: A string representing the path to the repository.
- project_hierarchy: A string representing the hierarchy of the project within the repository.

**Code Description**:
In this function, the provided repo_path is assigned to the self.repo_path attribute. Subsequently, a new jedi Project object is created using the repo_path and assigned to the self.project attribute. Additionally, the project_hierarchy is combined with the repo_path to create a full path to the project_hierarchy.json file, which is then assigned to the self.project_hierarchy attribute.

**Note**:
- Make sure to provide valid paths for repo_path and project_hierarchy parameters to ensure proper initialization of the ProjectManager object.
***
### FunctionDef get_project_structure(self)
**get_project_structure**: The function of get_project_structure is to retrieve the structure of the project by recursively traversing the directory tree.

**parameters**:
- No external parameters are required for this function.

**Code Description**:
The get_project_structure function defines an inner function walk_dir that recursively walks through the directory tree starting from the specified root directory (self.repo_path). It appends the directory names and Python files (.py) found in the project structure to a list called structure. The function ignores hidden files and directories that start with a dot.

**Note**:
- This function is designed to work within a ProjectManager object and relies on the repo_path attribute to determine the project's root directory.
- The function only considers directories and Python files (.py) in the project structure.

**Output Example**:
project_folder
  subfolder1
    file1.py
    file2.py
  subfolder2
    subfolder3
      file3.py
#### FunctionDef walk_dir(root, prefix)
**walk_dir**: The function of walk_dir is to recursively walk through a directory structure, ignoring hidden files and directories, and collecting Python files.

**parameters**:
· root: The root directory to start walking from.
· prefix: A string representing the current directory prefix.

**Code Description**:
The walk_dir function takes two parameters: root and prefix. It appends the base name of the root directory to the structure list. Then, it iterates over the sorted list of items in the root directory. If an item starts with a dot (indicating a hidden file or directory), it is skipped. For each item, if it is a directory, the function is called recursively with the new path and an updated prefix. If the item is a Python file (ends with ".py"), its name is appended to the structure list with the updated prefix.

**Note**:
Ensure that the root directory provided exists and is accessible for the function to walk through the directory structure.
***
***
### FunctionDef build_path_tree(self, who_reference_me, reference_who, doc_item_path)
**build_path_tree**: The function of build_path_tree is to construct a tree structure based on the provided paths and return a string representation of the tree.

**parameters**:
- who_reference_me: List of paths referencing the current object.
- reference_who: List of paths referenced by the current object.
- doc_item_path: Path of the document item.

**Code Description**: The build_path_tree function initializes a tree structure using defaultdict. It then builds a tree based on the paths provided in who_reference_me and reference_who lists. The function processes the doc_item_path by splitting it into parts and marking the last part with a star symbol. Finally, it converts the tree structure into a string representation recursively.

**Note**: Ensure that the paths provided are valid and correctly formatted to avoid errors in tree construction.

**Output Example**: 
```
    path1
        subpath1
            ✳️subsubpath1
            subsubpath2
        subpath2
    path2
        subpath1
```
#### FunctionDef tree
**tree**: The function of tree is to return a defaultdict initialized with the tree function.

**parameters**: 
- No parameters are required for this function.

**Code Description**: 
The tree function returns a defaultdict object initialized with the tree function. This allows for the creation of a nested structure where new keys are automatically created as defaultdict objects when accessed.

**Note**: 
It is important to note that defaultdict is a subclass of the built-in dict class in Python, providing a default value for keys that do not exist. The use of tree in this context allows for the creation of a nested structure with automatic key generation.

**Output Example**: 
A possible appearance of the return value:
defaultdict(<function tree at 0x000001>, {})
***
#### FunctionDef tree_to_string(tree, indent)
**tree_to_string**: The function of tree_to_string is to convert a nested dictionary representing a tree structure into a string with proper indentation.

**parameters**:
- tree: A nested dictionary representing a tree structure.
- indent: An integer representing the current level of indentation (default is 0).

**Code Description**:
The function iterates through the items of the input tree dictionary, sorts them, and then recursively builds a string representation of the tree with appropriate indentation based on the current level.

If the value of a key in the tree is another dictionary, the function calls itself recursively with the nested dictionary and increments the indentation level by 1.

The function then returns the final string representation of the tree.

**Note**:
- Make sure to pass a nested dictionary as the 'tree' parameter to get the correct string representation.
- The 'indent' parameter is used internally for proper indentation and should not be modified unless necessary.

**Output Example**:
```
root
    ├── child1
    │   ├── subchild1
    │   └── subchild2
    └── child2
```
***
***
