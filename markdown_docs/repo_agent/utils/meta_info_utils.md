## FunctionDef make_fake_files
**make_fake_files**: The function of make_fake_files is to detect staging area information based on the git status and perform specific actions on the files in the target repository. It handles new files, modified files, and deleted files that have not been added to the staging area.

**parameters**:
- None

**Code Description**:
The make_fake_files function first calls the delete_fake_files function to remove any existing fake files. It then initializes a git repository object using the target repository path obtained from the project settings.

Next, it retrieves the unstaged changes and untracked files from the git repository. Untracked files are files that exist in the file system but are not tracked by git. The function skips any untracked files with the ".py" extension and adds them to the jump_files list.

For newly added files (change type 'A'), the function checks if the file name ends with a specific substring (latest_version_substring). If it does, it logs an error message and exits the program. Otherwise, it adds the file path to the jump_files list.

The function then iterates over the modified and deleted files (change types 'M' and 'D') and performs the following actions:
- Checks if the file name ends with the latest_version_substring. If it does, it logs an error message and exits the program.
- Retrieves the current file path and checks if it ends with the ".py" extension.
- Reads the raw content of the file from the git status.
- Constructs the latest file path by replacing the ".py" extension with the latest_version_substring.
- If the current file path exists in the target repository, it renames it to the latest file path and logs a message indicating the action taken.
- If the current file path does not exist in the target repository, it creates a new file with the latest file path and logs a message indicating the action taken.
- Writes the raw file content to the current file path.
- Adds the current file path and the latest file path to the file_path_reflections dictionary, where the current file path is the key and the latest file path is the value.

Finally, the function returns the file_path_reflections dictionary and the jump_files list.

**Note**: It is important to use the delete_fake_files function after the documentation process to clean up any temporary or fake files generated during the execution.

**Output Example**:
{
    "file_path_1.py": "file_path_1_latest.py",
    "file_path_2.py": "file_path_2_latest.py",
    ...
}
[
    "jump_file_1.py",
    "jump_file_2.py",
    ...
]
## FunctionDef delete_fake_files
**delete_fake_files**: The function of delete_fake_files is to remove all fake files after the task execution is completed.

**parameters**: This Function does not take any parameters.

**Code Description**: The delete_fake_files function contains a nested function gci(filepath) that recursively traverses all files in the specified filepath, including subdirectories. Within gci, the function identifies directories and files ending with a specific substring (latest_version_substring). For files ending with the substring, it performs the following actions:
1. Replaces the substring with ".py" in the file name.
2. Deletes the original file.
3. If the file size is 0, it prints the target repository path and information about the deleted temporary file before removing it.
4. If the file size is not 0, it prints information about recovering the latest version by renaming the file.
5. Finally, it deletes the processed file.

The delete_fake_files function then calls the gci function with the target repository path obtained from the project settings.

In the project, delete_fake_files is called by the clean function in main.py to clean up fake files generated during the documentation process. Additionally, the run function in Runner class in runner.py calls delete_fake_files after completing the document update process to remove any remaining fake files.

**Note**: It is essential to use delete_fake_files after the documentation process to clean up any temporary or fake files generated during the execution.
### FunctionDef gci(filepath)
**gci**: The function of gci is to recursively traverse a specified filepath, delete temporary files, and recover the latest version of files.

**parameters**:
- filepath: The path to the directory to be traversed.

**Code Description**:
The gci function starts by listing all files in the specified filepath. It then iterates through each file in the directory. If the file is a directory, the function recursively calls itself on that directory. If the file ends with a specific substring (latest_version_substring), it performs the following actions:
1. Replaces the latest_version_substring with ".py" to get the original file name.
2. Deletes the original file.
3. If the file size is 0, prints the target repository path and deletes the temporary file.
4. If the file size is not 0, prints a message indicating the recovery of the latest version and renames the file to the original name.

**Note**:
- Ensure that the latest_version_substring is correctly defined before calling the gci function to avoid unexpected behavior.
- Be cautious when using this function as it involves deleting files from the specified directory.
***
