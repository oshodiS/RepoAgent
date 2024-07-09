## FunctionDef build_path_tree(who_reference_me, reference_who, doc_item_path)
**build_path_tree**: The function of build_path_tree is to construct a tree structure based on the provided paths and return a string representation of the tree.

**parameters**:
- who_reference_me: List of paths referencing the current object.
- reference_who: List of paths referencing other objects.
- doc_item_path: Path of the current object.

**Code Description**:
The function first defines a nested tree function using defaultdict to create a tree structure. It then iterates over the paths in who_reference_me and reference_who lists, splitting each path by the separator and creating nodes in the path_tree accordingly.

After processing the paths, the function modifies the doc_item_path by adding a symbol before the last part of the path. It then traverses the path_tree to reach the modified doc_item_path.

A tree_to_string function is defined to convert the tree structure into a string representation recursively, sorting the keys and adding appropriate indentation.

The function finally returns the string representation of the path_tree.

**Note**: 
- The function relies on the os module, so ensure it is imported before calling build_path_tree.
- Make sure to provide valid paths as input parameters to generate the desired tree structure.

**Output Example**:
```
root
    folder1
        subfolder1
            ✳️file1
    folder2
        subfolder2
            ✳️file2
```
### FunctionDef tree
**tree**: The function of tree is to return a defaultdict with the tree structure.

**parameters**: This Function does not take any parameters.

**Code Description**: The tree function creates and returns a defaultdict with the tree structure. This defaultdict allows for the creation of nested dictionaries without explicitly defining each level.

**Note**: When using this function, keep in mind that the returned defaultdict can be used to represent a tree-like structure where each key can have multiple sub-keys. This can be useful for organizing hierarchical data.

**Output Example**: 
A possible appearance of the return value:
defaultdict(<class 'function'>, {})
***
### FunctionDef tree_to_string(tree, indent)
**tree_to_string**: The function of tree_to_string is to convert a nested dictionary tree structure into a string representation with proper indentation.

**parameters**:
- tree: A nested dictionary representing the tree structure.
- indent: An integer representing the current level of indentation (default is 0).

**Code Description**:
The tree_to_string function takes a nested dictionary 'tree' and an optional 'indent' parameter to generate a string representation of the tree structure. It iterates through the items of the dictionary, sorts them, and appends each key to the string with the appropriate level of indentation. If the value corresponding to a key is another dictionary, the function recursively calls itself with the nested dictionary and increments the indentation level.

**Note**:
- The function assumes that the input 'tree' is a nested dictionary.
- The 'indent' parameter controls the level of indentation in the output string.
- Make sure to provide a valid nested dictionary as input to get the desired string representation.

**Output Example**:
```
root
    ├── child1
    │   ├── subchild1
    │   └── subchild2
    └── child2
```
***
