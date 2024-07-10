## FunctionDef build_path_tree(who_reference_me, reference_who, doc_item_path)
**build_path_tree**: The function of build_path_tree is to construct a tree structure based on the provided paths and return a string representation of the tree.

**parameters**:
- who_reference_me: List of paths referencing other items.
- reference_who: List of paths referenced by other items.
- doc_item_path: Path of the document item.

**Code Description**:
The function first defines a nested tree function using defaultdict to create a tree-like structure. It then iterates over the paths in who_reference_me and reference_who lists, splitting each path into parts and creating nodes in the path_tree based on these parts. After that, it processes the doc_item_path by splitting it into parts, marking the last part with a special symbol, and updating the path_tree accordingly. Finally, it converts the path_tree into a string representation using a recursive tree_to_string function and returns the string.

**Note**: 
- This function relies on the os module, so ensure that the os module is imported before using this function.
- Make sure to provide valid paths as input parameters to avoid errors in tree construction.

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
**tree**: The function of tree is to return a defaultdict with the tree as the default factory.

**parameters**: 
- No parameters are required for this function.

**Code Description**: 
The tree function utilizes the defaultdict class from the collections module in Python. By calling tree(), a defaultdict is returned with the tree function set as the default factory. This allows the defaultdict to create a nested structure where missing keys are automatically populated with defaultdict instances, effectively creating a tree-like data structure.

**Note**: 
It is important to note that this function is useful for creating and working with nested data structures in Python efficiently.

**Output Example**: 
defaultdict(<class 'function'>, {})
***
### FunctionDef tree_to_string(tree, indent)
**tree_to_string**: The function of tree_to_string is to convert a nested dictionary into a string representation with proper indentation.

**parameters**:
- tree: A nested dictionary to be converted into a string.
- indent: An integer representing the current level of indentation (default is 0).

**Code Description**:
The function iterates through the items of the input dictionary in sorted order. For each key-value pair, it appends the key with the appropriate level of indentation to the output string. If the value is another dictionary, the function recursively calls itself with the nested dictionary and increments the indentation level. This process continues until all nested dictionaries are converted into the string representation.

**Note**:
- Make sure to provide a nested dictionary as input to properly utilize this function.
- The function uses recursion to handle nested dictionaries, so ensure that the input dictionary is not too deeply nested to avoid potential stack overflow issues.

**Output Example**:
```
root
    folder1
        file1
        file2
    folder2
        subfolder1
            file3
```
***
