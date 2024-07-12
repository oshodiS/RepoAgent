## FunctionDef create_readme_if_not_exist(dire)
**create_readme_if_not_exist**: The function of create_readme_if_not_exist is to create a README.md file in the specified directory if it does not already exist.

**parameters**:
- dire: The directory path where the README.md file should be created.

**Code Description**:
The create_readme_if_not_exist function first constructs the path to the README.md file within the specified directory. It then checks if the README.md file already exists in that directory. If the file does not exist, the function opens the README.md file in write mode and writes the directory name as a header in the markdown format.

This function is called by the output_markdown function in the project. In the output_markdown function, create_readme_if_not_exist is used to ensure that each directory has a README.md file. If the README.md file does not exist in a directory, create_readme_if_not_exist is called to create one. This helps in organizing and documenting the contents of the directories in the project.

**Note**:
- It is important to provide the correct directory path as the parameter to ensure the README.md file is created in the intended location.
## FunctionDef output_markdown(dire, base_dir, output_file, iter_depth)
**output_markdown**: The function of output_markdown is to generate a markdown summary of the contents in a specified directory and its subdirectories.

**parameters**:
- dire: The directory path to be processed.
- base_dir: The base directory path.
- output_file: The file object to write the markdown summary.
- iter_depth: The depth of iteration in the directory structure (default is 0).

**Code Description**:
The output_markdown function iterates through the files and directories in the specified directory. It first checks if a README.md file exists in each directory and creates one if it does not. Then, it processes the files and directories to generate a markdown summary. For directories, it creates a markdown link to the README.md file if present, and recursively calls itself for nested directories. For files, it checks if the file is a Markdown file and includes it in the summary if it meets certain conditions.

This function interacts with the create_readme_if_not_exist function to ensure each directory has a README.md file for documentation. Additionally, it utilizes the is_markdown_file function to identify Markdown files before including them in the summary.

**Note**:
- Ensure to provide the correct directory paths to dire and base_dir parameters.
- The iter_depth parameter is used internally for indentation in the markdown summary.
- It is important to maintain the integrity of the directory structure for accurate summary generation.
## FunctionDef markdown_file_in_dir(dire)
**markdown_file_in_dir**: The function of markdown_file_in_dir is to check if there are any Markdown (.md) or Markdown (.markdown) files present in a specified directory.

**parameters**:
- dire: A string representing the directory path to be checked for Markdown files.

**Code Description**:
The function markdown_file_in_dir takes a directory path as input and uses the os.walk method to traverse through all the files in the directory and its subdirectories. It then iterates over each file and checks if the file has a ".md" or ".markdown" extension using a regular expression. If it finds any file with the specified extensions, it returns True. If no Markdown files are found in the directory, the function returns False.

**Note**:
- Make sure to provide a valid directory path as the input parameter.
- The function only checks for files with ".md" or ".markdown" extensions and does not consider other file types.

**Output Example**:
True
## FunctionDef is_markdown_file(filename)
**is_markdown_file**: The function of is_markdown_file is to check if a given filename corresponds to a Markdown file by matching the file extension.

**parameters**:
- filename: A string representing the name of the file to be checked.

**Code Description**:
The `is_markdown_file` function uses a regular expression to search for the file extension '.md' or '.markdown' at the end of the filename. If a match is found, the function returns either the filename without the extension or False based on the length of the matched group.

When called, the function first searches for the file extension in the given filename. If a match is not found, it returns False. If a match is found, it then checks the length of the matched group to determine if it corresponds to '.md' or '.markdown'. If the length matches '.md', it returns the filename without the '.md' extension. If the length matches '.markdown', it returns the filename without the '.markdown' extension.

The function is utilized in the `output_markdown` function to determine if a file is a Markdown file before processing it further. If the file is a Markdown file and meets certain conditions, a markdown link to the file is created in the output.

**Note**:
- Ensure the filename is a string.
- The function only checks for the file extension and does not validate the file content.

**Output Example**:
If the input filename is 'example.md', the function will return 'example'.
## FunctionDef main
**main**: The function of main is to create a markdown summary file for a specified book directory.

**parameters**:
- No parameters are directly passed to the main function. It retrieves the book name from the command line arguments.

**Code Description**:
The main function first extracts the book name from the command line arguments. It then creates a directory path for the book within the 'books' directory. If the directory does not exist, it creates one. Subsequently, it creates a SUMMARY.md file within the book directory and writes a header for the summary. Finally, it calls the output_markdown function to generate the detailed markdown summary of the book contents.

The output_markdown function iterates through the files and directories in the specified book directory, creating markdown links for directories with README.md files and including Markdown files in the summary. It ensures each directory has a README.md file for documentation and identifies Markdown files before adding them to the summary.

The main function concludes by printing a message indicating the completion of the GitBook auto summary process.

**Note**:
- Ensure to provide the book name as a command line argument when executing the script.
- The output summary file will be named SUMMARY.md and will be located within the 'books' directory under the specified book name.
- The integrity of the book directory structure is crucial for accurate summary generation.

**Output Example**:
GitBook auto summary finished:)
