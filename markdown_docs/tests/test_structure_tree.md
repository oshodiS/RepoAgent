## FunctionDef build_path_tree(who_reference_me, reference_who, doc_item_path)
**build_path_tree**: The function of build_path_tree is to construct a tree structure based on provided paths and return it as a string representation.

**parameters**:
- who_reference_me: List of paths referencing the current item.
- reference_who: List of paths referenced by the current item.
- doc_item_path: Path of the current item.

**Code Description**:
The function first initializes a tree structure using defaultdict. It then iterates over the paths in who_reference_me and reference_who, splitting each path into parts and creating nodes in the tree accordingly. After that, it processes the doc_item_path by splitting it into parts, marking the last part with a special symbol, and updating the corresponding node in the tree. Finally, it recursively converts the tree structure into a string representation.

**Note**: Make sure to provide valid paths and handle path separators appropriately for the function to work correctly.

**Output Example**:
```
    who_reference_me
        path1
            subpath1
            subpath2
        path2
            subpath1
    reference_who
        path3
            subpath1
    ✳️doc_item_path
        subpath1
```
### FunctionDef tree
**tree**: The function of tree is to create a nested defaultdict structure.

**parameters**: 
- No parameters are required for this function.

**Code Description**: 
The tree function returns a nested defaultdict structure. This structure allows for the creation of a tree-like data structure where each level can have multiple branches. The defaultdict ensures that any key that does not exist is automatically created with a default value of another tree structure, enabling the dynamic creation of nested levels.

**Note**: 
This function is useful for creating hierarchical data structures or organizing data in a tree format.

**Output Example**: 
A possible appearance of the return value:
defaultdict(<class 'function'>, {})
***
### FunctionDef tree_to_string(tree, indent)
**tree_to_string**: The function of tree_to_string is to convert a nested dictionary representing a tree structure into a string with proper indentation.

**parameters**:
- tree: A nested dictionary representing a tree structure.
- indent: An integer representing the current level of indentation (default is 0).

**Code Description**:
The function iterates through the keys and values of the input dictionary in sorted order. For each key, it appends the key to the string with the appropriate level of indentation. If the corresponding value is a dictionary, the function recursively calls itself with the nested dictionary and increases the indentation level. This process continues until all nested dictionaries are traversed.

**Note**:
- Make sure the input tree is a nested dictionary structure for proper conversion.
- The function uses recursion to handle nested dictionaries, so ensure the depth of the tree is within the recursion limit to avoid stack overflow errors.

**Output Example**:
```
root
    child1
        subchild1
        subchild2
    child2
        subchild3
```
***
