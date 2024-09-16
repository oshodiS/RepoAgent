## FunctionDef create_readme_if_not_exist(dire)
**create_readme_if_not_exist**: The function of create_readme_if_not_exist is to create a README.md file in a specified directory if it does not already exist.

**parameters**:
- dire: The directory path where the README.md file should be created.

**Code Description**:
The create_readme_if_not_exist function first constructs the path to the README.md file within the specified directory. It then checks if the README.md file already exists in that directory. If the file does not exist, the function opens the README.md file in write mode and writes the directory name as a header in the file.

This function is called within the output_markdown function, which iterates through files and directories in a given directory. For each directory encountered, it ensures that a README.md file is created if it does not already exist. This is essential for generating documentation and markdown files for the project.

**Note**:
It is important to provide the correct directory path as the parameter when calling the create_readme_if_not_exist function to ensure the README.md file is created in the intended location.
## FunctionDef output_markdown(dire, base_dir, output_file, iter_depth)
**output_markdown**: The function of output_markdown is to generate a markdown summary of files and directories within a specified directory, including creating markdown links to README.md files and markdown files.

**parameters**:
- dire: The directory path to be processed.
- base_dir: The base directory path for relative path calculation.
- output_file: The output file to write the markdown summary.
- iter_depth: The iteration depth for nested directories (default is 0).

**Code Description**:
The output_markdown function iterates through the files and directories in the specified directory. For each directory encountered, it checks if a README.md file exists and creates one if not present. It then generates markdown links to README.md files and markdown files within the directory structure. If nested directories are found, the function recursively calls itself to process them as well.

Within the function, the create_readme_if_not_exist function is called to ensure README.md files are created where needed. Additionally, the is_markdown_file function is utilized to identify markdown files based on their extensions before including them in the markdown summary.

The function plays a crucial role in generating a structured markdown summary of the project's files and directories, facilitating documentation and navigation within the project.

**Note**:
- When using output_markdown, provide the correct directory paths to ensure accurate markdown summary generation.
- The function relies on the create_readme_if_not_exist and is_markdown_file functions for specific operations, ensuring proper file handling and markdown link creation.
## FunctionDef markdown_file_in_dir(dire)
**markdown_file_in_dir**: The function of markdown_file_in_dir is to check if there are any Markdown (.md) or Markdown (.markdown) files present in a specified directory.

**parameters**:
- dire: A string representing the directory path to be checked for Markdown files.

**Code Description**:
The function markdown_file_in_dir takes a directory path as input and uses the os.walk method to traverse through all the files in the directory and its subdirectories. It then iterates through each file and checks if the file name ends with '.md' or '.markdown' using a regular expression. If it finds any file with a matching extension, it returns True. If no Markdown files are found, it returns False.

**Note**:
- Make sure to provide a valid directory path as the input parameter to ensure accurate results.
- The function only checks for files with '.md' or '.markdown' extensions specifically.

**Output Example**:
True
## FunctionDef is_markdown_file(filename)
**is_markdown_file**: The function of is_markdown_file is to determine if a given filename corresponds to a Markdown file based on its extension.

**parameters**:
- filename: A string representing the name of the file to be checked.

**Code Description**:
The `is_markdown_file` function uses a regular expression to search for the file extension '.md' or '.markdown' at the end of the filename. If a match is found, the function returns either the filename without the extension if it matches '.md', or the filename without the extension if it matches '.markdown'. If no match is found, the function returns False.

In the calling object `output_markdown`, the `is_markdown_file` function is used to check if a file is a Markdown file before processing it. If the file is a Markdown file and meets certain conditions, a markdown link to the file is created in the output.

**Note**:
- Ensure that the filename parameter is a string representing a valid file name.
- The function relies on the file extension to determine if it is a Markdown file, so filenames without the correct extension may not be recognized.

**Output Example**:
If the input filename is 'example.md', the function will return 'example'.
If the input filename is 'document.markdown', the function will return 'document'.
## FunctionDef main
**main**: The function of main is to create a markdown summary of files and directories within a specified directory and write the summary to a file named SUMMARY.md.

**parameters**:
- book_name: The name of the book to generate the summary for.
- dir_input: The directory path for the book's source files.
- output_path: The path to the SUMMARY.md file.

**Code Description**:
The main function takes the book_name as a command-line argument, creates a directory structure for the book, and generates a markdown summary of the book's contents. It first creates the necessary directory structure, then opens the SUMMARY.md file within the book's source directory. The function then writes a header to the SUMMARY.md file and calls the output_markdown function to generate the markdown summary based on the book's source files.

The output_markdown function recursively processes the files and directories within the specified directory, creating markdown links to README.md files and markdown files. This process ensures a structured summary of the book's contents is generated in the SUMMARY.md file.

Upon completion, the main function prints a message indicating the successful generation of the GitBook auto summary.

**Note**:
- Ensure to provide the correct book_name as a command-line argument when executing the main function.
- The function relies on the output_markdown function to generate the markdown summary, which in turn handles the detailed processing of files and directories.
- The generated SUMMARY.md file serves as a structured overview of the book's contents for documentation and navigation purposes.

**Output Example**:
# Summary

- [Chapter 1](src/chapter1.md)
  - [Section 1](src/chapter1/section1.md)
  - [Section 2](src/chapter1/section2.md)
- [Chapter 2](src/chapter2.md)
  - [Section 1](src/chapter2/section1.md)
  - [Section 2](src/chapter2/section2.md)

GitBook auto summary finished:)
