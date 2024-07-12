## FunctionDef main
**main**: The function of main is to copy Markdown documents from a specified folder to a destination folder, create a README.md file if it does not exist, and organize the copied documents accordingly.

**parameters**:
- markdown_docs_folder: The folder containing the Markdown documents to be copied.
- book_name: The name of the book where the documents will be copied.
- repo_path: The path to the repository where the Markdown documents are located.

**Code Description**:
The main function first creates a destination directory for the book in the './books' folder. It then checks if the destination directory exists and creates it if not. Next, it iterates through the files and folders in the specified Markdown documents directory, copies them to the destination directory, and prints the actions taken (copying a file or a folder). After copying all the documents, it checks if a README.md file exists in the destination directory and creates one with the book name if it does not.

**Note**:
- Ensure that the correct arguments are passed when calling the main function (markdown_docs_folder, book_name, repo_path).
- The function assumes the existence of the './books' directory for organizing the copied documents.
- It is important to have the necessary permissions to create directories and files in the specified locations.
### FunctionDef create_book_readme_if_not_exist(dire)
**create_book_readme_if_not_exist**: The function of create_book_readme_if_not_exist is to create a README.md file in the specified directory if it does not already exist.

**parameters**:
- dire: A string representing the directory path where the README.md file should be created.

**Code Description**:
The function first constructs the path to the README.md file by joining the provided directory path with the filename 'README.md'. It then checks if a file already exists at that path. If the file does not exist, it creates a new README.md file in the specified directory and writes a header containing the book name.

**Note**:
- Ensure that the 'book_name' variable is defined and accessible within the scope of the function before calling create_book_readme_if_not_exist.
- Make sure to handle any potential exceptions related to file operations or directory paths when using this function.
***
