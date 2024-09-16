## FunctionDef build_path_tree(who_reference_me, reference_who, doc_item_path)
**build_path_tree**: The function of build_path_tree is to construct a tree structure based on provided paths and return a string representation of the tree.

**parameters**:
- who_reference_me: List of paths referencing other items.
- reference_who: List of paths referenced by other items.
- doc_item_path: Path of the document item.

**Code Description**:
The function first defines a nested tree function using defaultdict to create a tree-like structure. It then iterates over the paths in who_reference_me and reference_who lists, splitting each path into parts and creating nodes in the path_tree accordingly. After that, it processes the doc_item_path by splitting it into parts, marking the last part with a star symbol, and updating the path_tree structure. Finally, it converts the path_tree into a string representation using a recursive tree_to_string function and returns the string.

**Note**: 
- This function relies on the os module, so make sure to import it before using build_path_tree.
- Ensure the paths provided are valid and correctly formatted to avoid errors in tree construction.

**Output Example**:
```
root
    folder1
        file1
        file2
    folder2
        ✳️file3
```
### FunctionDef tree
**tree**: The function of tree is to return a defaultdict initialized with the tree function.

**parameters**: This Function does not take any parameters.

**Code Description**: The tree function creates and returns a defaultdict object that is recursively initialized with the tree function. This allows for the creation of a nested data structure that can be dynamically expanded as needed.

**Note**: This function is useful for creating hierarchical data structures where the depth of the structure is not predefined. It provides a flexible way to work with nested data in Python.

**Output Example**: 
A possible appearance of the return value when calling the tree function:
defaultdict(<function tree at 0x000001>, {})
***
### FunctionDef tree_to_string(tree, indent)
**tree_to_string**: The function of tree_to_string is to convert a nested dictionary tree structure into a string representation with proper indentation.

**parameters**:
- tree: A nested dictionary representing the tree structure.
- indent: An integer representing the current level of indentation (default is 0).

**Code Description**:
The tree_to_string function takes a nested dictionary 'tree' and an optional 'indent' parameter to generate a string representation of the tree structure. It iterates through the items of the dictionary, sorts them, and appends each key to the string with the appropriate level of indentation. If the value of a key is another dictionary, the function recursively calls itself with the nested dictionary and increments the indentation level. The process continues until all nested dictionaries are processed, and the final string representation of the tree is returned.

**Note**:
- Make sure to provide a valid nested dictionary as input to the function to get the desired string representation.
- The function uses recursion to handle nested dictionaries, so be cautious with deeply nested structures to avoid potential stack overflow errors.

**Output Example**:
```
root
    ├── child1
    │   ├── subchild1
    │   └── subchild2
    └── child2
```
***
