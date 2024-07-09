## FunctionDef create_readme_if_not_exist(dire)
**create_readme_if_not_exist**: The function of create_readme_if_not_exist is to create a README.md file in a specified directory if it does not already exist.

**parameters**:
- dire: The directory path where the README.md file should be created.

**Code Description**:
The create_readme_if_not_exist function first constructs the path to the README.md file within the specified directory. It then checks if the README.md file already exists in that directory. If the file does not exist, it opens the README.md file in write mode and writes the directory name as a header in markdown format.

This function is called within the output_markdown function, which iterates through files and directories in a given directory. For each directory encountered, it ensures a README.md file is created if it does not exist. This is useful for maintaining a structured documentation system within directories.

**Note**:
Ensure that the directory path provided as input exists before calling the create_readme_if_not_exist function to avoid any errors.
## FunctionDef output_markdown(dire, base_dir, output_file, iter_depth)
**output_markdown**: The function of output_markdown is to generate a markdown summary of files and directories within a specified directory, including creating markdown links to README.md files and markdown files.

**parameters**:
- dire: The directory path to be processed.
- base_dir: The base directory path for relative referencing.
- output_file: The output file object to write the markdown summary.
- iter_depth: The iteration depth for nested directories (default is 0).

**Code Description**:
The output_markdown function iterates through the files and directories in the specified directory. It first ensures that a README.md file is created for each directory if it does not already exist by calling the create_readme_if_not_exist function. Then, it processes each file and directory, creating markdown links in the output_file for README.md files and markdown files found. For directories, it recursively calls itself to handle nested directories.

The function also utilizes the is_markdown_file function to check if a file is a Markdown file before including it in the markdown summary. It excludes certain files like 'SUMMARY.md' and 'README.md' based on the iteration depth to maintain the summary's structure.

**Note**:
- Ensure that the directory paths provided exist before calling the output_markdown function.
- The function relies on the create_readme_if_not_exist and is_markdown_file functions for specific tasks within the markdown generation process.
## FunctionDef markdown_file_in_dir(dire)
**markdown_file_in_dir**: The function of markdown_file_in_dir is to check if there are any Markdown (.md) or Markdown (.markdown) files in a specified directory.

**parameters**:
- dire: A string representing the directory path to be checked for Markdown files.

**Code Description**:
The function markdown_file_in_dir takes a directory path as input and uses the os.walk method to traverse through all the files in the directory and its subdirectories. It then iterates over each file and checks if the file name ends with '.md' or '.markdown' using a regular expression. If such a file is found, the function returns True. If no Markdown files are found in the directory, the function returns False.

**Note**:
- Make sure to provide a valid directory path as input to the function.
- The function only checks for files with '.md' or '.markdown' extensions, not the content of the files.

**Output Example**:
True
## FunctionDef is_markdown_file(filename)
**is_markdown_file**: The function of is_markdown_file is to check if a given filename corresponds to a Markdown file based on its extension.

**parameters**:
- filename: A string representing the name of the file to be checked.

**Code Description**:
The is_markdown_file function uses a regular expression to search for the file extension '.md' or '.markdown' at the end of the filename. If a match is found, the function returns the filename without the extension if it matches either '.md' or '.markdown'.

In the calling object output_markdown, the is_markdown_file function is used to determine if a file is a Markdown file before processing it further. If the file is a Markdown file and meets certain conditions, a markdown link to the file is created in the output.

**Note**:
- Ensure that the filename parameter is a valid string representing a file name.
- The function only checks for the presence of '.md' or '.markdown' at the end of the filename to determine if it is a Markdown file.

**Output Example**:
If the input filename is 'example.md', the function will return 'example'.
## FunctionDef main
**main**: The function of main is to create a markdown summary file for a specified book directory, including markdown links to relevant files and directories.

**parameters**:
- book_name: The name of the book directory.
  
**Code Description**:
The main function first creates a directory path for the book folder within the 'books' directory. It then checks if the directory exists and creates it if not. Subsequently, it creates a SUMMARY.md file within the book directory and writes a header for the summary. The function then calls the output_markdown function to generate the markdown summary based on the contents of the book directory. Finally, it prints a message indicating the completion of the GitBook auto summary process.

In this process, the main function relies on the output_markdown function to handle the markdown generation logic, ensuring that the summary includes relevant markdown links to README.md files and markdown files within the book directory.

**Note**:
- Ensure that the book directory path provided as an argument exists before executing the main function.
- The main function is essential for initiating the markdown summary generation process for a book directory.

**Output Example**:
# Summary

- [file1.md](./books/book_name/src/file1.md)
- [file2.md](./books/book_name/src/file2.md)
- [directory1](./books/book_name/src/directory1/README.md)
  - [file3.md](./books/book_name/src/directory1/file3.md)
  - [directory2](./books/book_name/src/directory1/directory2/README.md)
    - [file4.md](./books/book_name/src/directory1/directory2/file4.md)
GitBook auto summary finished:)
