## FunctionDef language_prompt(default_language)
**language_prompt**: The function of language_prompt is to prompt the user to enter a language (ISO 639 code or language name) and return the corresponding language name.

**parameters**:
- default_language: The default language to be displayed in the prompt.

**Code Description**: 
The `language_prompt` function utilizes the `click.prompt` method to request the user to input a language in the form of an ISO 639 code or language name. It then attempts to match the input with a language name using the `Language.match` method. If a match is found, the function returns the language name. If no match is found, it raises a `LanguageNotFoundError` exception and displays an error message.

In the project, this function is called within the `configure` function in order to set the language parameter for the agent's project settings. By invoking `language_prompt` with the default language from the project settings, the user is prompted to provide a language input, which is then used to configure the language setting for the agent.

**Note**: 
- Ensure that the input language provided by the user is either an ISO 639 code or a valid language name to avoid errors.
- Handle the `LanguageNotFoundError` exception to manage cases where the input language is not recognized.

**Output Example**: 
If the user enters 'en' as the language code, the function will return 'English' as the language name.
## FunctionDef cli
**cli**: The function of cli is to serve as an LLM-Powered Framework for Repository-level Code Documentation Generation.

**parameters**: 
- This function does not take any parameters.

**Code Description**: 
The `cli` function is designed to provide a framework for generating code documentation at the repository level using LLM technology. The function itself does not contain any specific implementation details but acts as a starting point for initiating the code documentation generation process within the repository.

**Note**: 
Developers can call the `cli` function from the main script of the repository to kickstart the code documentation generation process. The function is a key component in utilizing LLM technology for efficient and effective documentation of code within the repository.
## FunctionDef configure
**configure**: The function of configure is to configure the agent's parameters.

**parameters**:
- No parameters are explicitly defined for this function.

**Code Description**:
The `configure` function is responsible for configuring the agent's parameters. It prompts the user to input various settings related to the agent's project and chat completion functionality. These settings include the target repository path, project hierarchy file name, Markdown documents folder name, files or directories to ignore, language, maximum number of threads, maximum number of document tokens, and log level.

The function utilizes the `click.prompt` method from the `click` library to prompt the user for input. It provides default values for some settings, allowing the user to accept the defaults or enter their own values. The user's input is then used to instantiate objects of the `ProjectSettings` and `ChatCompletionSettings` classes, which store the respective settings.

After the settings are collected, the function creates a `Setting` object by passing the `ProjectSettings` and `ChatCompletionSettings` instances as arguments. This `Setting` object represents the combined project and chat completion settings.

The function also calls the `write_config` function to update the configuration file with the new settings. This ensures that the agent's parameters are saved and can be used in subsequent runs of the program.

The `configure` function provides feedback to the user by logging success messages using the `logger.success` method.

**Relationship with Callers**:
The `configure` function is called within the project's main program logic, typically from the `run` function in `main.py`. It is used to collect and save the project and chat completion settings before executing the main program logic. The `write_config` function is invoked within `configure` to update the configuration file with the new settings.

**Note**:
- Ensure that the user provides valid inputs for each setting to avoid errors during configuration.
- The `write_config` function is responsible for updating the configuration file with the new settings. Refer to the documentation for `write_config` for more details on its functionality and usage.
- The success messages logged by the `logger.success` method indicate that the project and chat completion settings were saved successfully.
## FunctionDef run(model, temperature, request_timeout, base_url, target_repo_path, hierarchy_path, markdown_docs_path, ignore_list, language, log_level)
**run**: The `run` function is responsible for executing the main program logic with the specified parameters.

**parameters**:
- `model`: A string representing the model to be used for chat completion.
- `temperature`: A positive float value indicating the randomness of the chat completion responses.
- `request_timeout`: A positive float value representing the timeout duration for API requests.
- `base_url`: A URL string specifying the base URL for API requests.
- `target_repo_path`: A string representing the path to the target repository.
- `hierarchy_path`: A string representing the name of the project hierarchy file.
- `markdown_docs_path`: A string representing the name of the folder to store the generated Markdown documents.
- `ignore_list`: A list of strings representing the files or directories to ignore during documentation generation.
- `language`: A string representing the language used for the documentation.
- `log_level`: An instance of the LogLevel class representing the log level for the program.

**Code Description**:
The `run` function starts by recording the start time using the `time` module. It then initializes the `project_settings` object with the provided parameters, including the target repository path, project hierarchy name, Markdown documents folder name, ignore list, language, and log level.

Next, the function creates a `chat_completion_settings` object with the provided model, temperature, request timeout, and base URL.

The `settings` object is then created, combining the `project_settings` and `chat_completion_settings` objects.

The function proceeds to write the configuration settings to a file using the `write_config` function from the `config_manager.py` module. This ensures that the program settings are saved for future use.

The log level for the logger is set based on the `log_level` parameter using the `set_logger_level_from_config` function from the `log.py` module.

A `runner` object is instantiated from the `Runner` class.

The `run` method of the `runner` object is called, which performs the main document update process. This includes generating and updating documentation for the target repository, detecting changes in the repository, and running the document update process.

After the document update process is completed, a success message is logged using the `logger` object.

Finally, the elapsed time is calculated and logged using the `logger` object.

**Note**:
- Ensure that the provided parameters are valid and appropriate for the intended use.
- The `write_config` function is responsible for updating the configuration file with the provided settings.
- The `set_logger_level_from_config` function sets the log level for the logger based on the provided configuration.
- The `Runner` class is responsible for managing the document generation and update process.
- The `run` method of the `Runner` class handles the main logic for generating and updating documentation.
- The `logger` object is used to log messages and provide information about the document generation process.
- The elapsed time is calculated to provide an indication of the time taken for the document generation process.
## FunctionDef clean
**clean**: The function of clean is to clean the fake files generated by the documentation process.

**parameters**: This Function does not take any parameters.

**Code Description**: The `clean` function initiates the cleaning process by calling the `delete_fake_files` function, which is responsible for removing all fake files generated during the documentation process. Once the fake files are deleted, the function logs a success message using the `logger.success` method, indicating that the fake files have been successfully cleaned up.

The `delete_fake_files` function, in turn, defines an inner function `gci` to traverse through all files in a specified filepath, identifying fake files based on a specific substring. It then performs actions such as replacing the fake file extension, deleting the original fake file if its size is 0, or recovering the latest version by renaming the fake file. Messages are printed to inform about the actions taken on the fake files.

In the project, the `delete_fake_files` function is called in various contexts to ensure the integrity of the document generation process:
1. It is called in the `make_fake_files` function to clean fake files before detecting staging area information based on git status.
2. It is used in the `diff` function to delete fake files before checking for changes and updating or generating documents.
3. It is invoked in the `run` method of the `Runner` class after the document update process to delete fake files.

**Note**: It is crucial to utilize the `delete_fake_files` function when dealing with fake files to maintain the accuracy and reliability of the document generation process.
## FunctionDef print_hierarchy
**print_hierarchy**: The function of print_hierarchy is to print the hierarchy of the target repository.

**parameters**:
- self: The current instance of the class.
- indent (optional): An integer representing the current level of indentation. The default value is 0.
- print_content (optional): A boolean indicating whether to print the content of the objects. The default value is False.
- diff_status (optional): A boolean indicating whether to print the difference status of the objects. The default value is False.
- ignore_list (optional): A list of strings representing file paths to be ignored during printing. The default value is an empty list.

**Code Description**:
The print_hierarchy function is a recursive function that prints the repository objects in a hierarchical manner. It takes several optional parameters to control the printing behavior.

The function first defines a nested helper function called print_indent, which is used to generate the indentation string based on the current level of indentation. The indentation string is calculated by multiplying the indent parameter by two spaces and adding a "|-" character at the beginning.

Next, the function determines the name to be printed for the current object. If the item_type attribute of the current object is DocItemType._repo, the name is set to the target repository name specified in the setting.project.target_repo variable. Otherwise, the name is set to the obj_name attribute of the current object.

If the diff_status parameter is True and the need_to_generate function returns True for the current object, indicating that the documentation needs to be generated or updated, the function prints the object type, name, and item status using the print_indent function for indentation.

If the diff_status parameter is False or the need_to_generate function returns False, the function prints only the object type and name using the print_indent function for indentation.

The function then iterates through the children of the current object and recursively calls the print_recursive function on each child, incrementing the indent parameter by 1. If the diff_status parameter is True and the child object does not have a task, indicating that it does not need to be generated or updated, the function skips printing the child.

The print_recursive function is primarily used in the print_hierarchy function and the diff function in the main.py file. In the print_hierarchy function, it is called on the target_repo_hierarchical_tree object of the MetaInfo class to print the hierarchy of the target repository. In the diff function, it is called on the target_repo_hierarchical_tree object of the new_meta_info variable to print the documents that will be generated or updated.

**Note**:
- The print_recursive function is used to recursively print the repository objects with proper indentation and formatting.
- It takes several optional parameters to control the printing behavior, such as the level of indentation, whether to print the content of the objects, whether to print the difference status of the objects, and a list of file paths to be ignored during printing.
- The function uses the print_indent helper function to generate the indentation string.
- It determines the name to be printed for each object based on its item_type attribute.
- The function checks the diff_status parameter and the result of the need_to_generate function to decide whether to print the object's item status.
- It recursively calls itself on the children of each object to print the hierarchy.
- The print_recursive function is called in the print_hierarchy and diff functions in the main.py file to print the hierarchy of the target repository and the documents that will be generated or updated, respectively.

**Output Example**:
```
|-_dir: directory_name
  |-_file: file_name
    |-_class: class_name
      |-_function: function_name
      |-_sub_function: sub_function_name
  |-_file: file_name
    |-_class: class_name
      |-_class_function: class_function_name
```

**Note**: During the document update process, the target repository code should not be modified. The generation process of a document is bound to a specific version of the code.
## FunctionDef diff
An unknown error occurred while generating this documentation after many tries.
## FunctionDef chat_with_repo(chunk_size, chunk_overlap)
**chat_with_repo**: The function of chat_with_repo is to initiate an automatic question and answer session for documentation explanation.

**parameters**:
- chunk_size: The size of data chunks for processing.
- chunk_overlap: The overlap between data chunks.

**Code Description**:
The chat_with_repo function facilitates an interactive chat session with a repository by configuring the necessary paths and parameters. It first checks the existence of markdown documents at the specified location and then initializes a ChatRepo instance with the provided settings. The chat session is started, allowing users to input questions related to documentation, which are processed and answered automatically based on the integrated models.

The ChatRepo class, which is called within the chat_with_repo function, manages the chat session by utilizing specific and general models to classify and respond to user queries effectively. By leveraging the start_chat method of the ChatRepo class, users can engage in a dynamic conversation with the chatbot, receiving relevant answers to their questions in real-time.

**Note**:
Ensure that the markdown documents and project hierarchy file are available at the designated paths for seamless operation of the chat session. Adjusting the chunk size and overlap parameters can influence the processing of user queries and the generation of automated responses during the interactive chat experience.
## FunctionDef show_chunk(chunk_size, chunk_overlap)
**show_chunk**: The function of show_chunk is to display how a document is chunked and save the chunking result to a file.

**parameters**:
- chunk_size: The size of each chunk to be created.
- chunk_overlap: The number of characters to overlap between consecutive chunks.

**Code Description**:
The show_chunk function takes the chunk_size and chunk_overlap parameters to display the chunking process of a document. It utilizes the SpecificModel class to get the chunked documents using the get_chunk_docs function. The chunking result is then saved to a file named "chunking_result.txt" for further reference. This function provides a way to visualize and store the chunked content of documents efficiently.

**Note**:
- Ensure to set appropriate values for chunk_size and chunk_overlap to control the chunking process effectively.
- The output of the show_chunk function can be used for various purposes such as text analysis or data processing.
