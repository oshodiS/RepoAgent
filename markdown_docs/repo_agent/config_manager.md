## FunctionDef get_config_path
**get_config_path**: The function of get_config_path is to retrieve the path to the configuration file used by the application.

**parameters**:
- No parameters are passed to this function.

**Code Description**:
The `get_config_path` function first checks the current working directory for a configuration file named `config.toml`. If the file exists in the current directory, the function returns the path to this file. If the file is not found in the current directory, the function determines the appropriate configuration path based on the operating system:
- For Unix and macOS systems, it uses the home directory.
- For Windows systems, it uses the APPDATA directory.
- If the operating system detection fails, it defaults to a local directory within the current working directory.
The function ensures that the configuration directory exists and creates an empty configuration file if it does not already exist. Finally, it returns the complete path to the configuration file.

**Relationship with Callers**:
The `get_config_path` function is called by other functions within the `config_manager.py` module, such as `read_config` and `write_config`. These functions rely on `get_config_path` to obtain the correct path to the configuration file before reading from or writing to it.

**Note**:
- This function does not accept any parameters and operates based on the current working directory and the operating system to determine the configuration file path.
- It is essential to ensure that the necessary permissions are granted for the function to create or modify files in the specified configuration directory.

**Output Example**:
If the configuration file is located in the current working directory, the function will return a `Path` object representing the path to the `config.toml` file.
## FunctionDef read_config(file_path)
**read_config**: The function of read_config is to read a configuration file specified by the file_path parameter or determine the path using get_config_path function if no file_path is provided, and return the contents of the configuration file as a dictionary.

**parameters**:
- file_path: Optional parameter representing the path to the configuration file. If not provided, it defaults to None.

**Code Description**:
The read_config function first checks if a file_path is provided. If not, it calls the get_config_path function to determine the configuration file path. It then opens the configuration file, reads its contents using the tomli library, and returns the configuration data as a dictionary. In case of any decoding errors, an empty dictionary is returned.

**Relationship with Callers**:
The read_config function is typically called by other parts of the application that require access to configuration settings. It relies on the get_config_path function to obtain the correct path to the configuration file before reading its contents.

**Note**:
- The read_config function can handle both cases where a file_path is provided and where it is not, ensuring flexibility in configuration file retrieval.
- It is important to handle any potential decoding errors that may occur when reading the configuration file.

**Output Example**:
If the configuration file contains the following data:
```python
{
    "key1": "value1",
    "key2": 123,
    "key3": ["a", "b", "c"]
}
```
The read_config function will return:
```python
{
    "key1": "value1",
    "key2": 123,
    "key3": ["a", "b", "c"]
}
```
## FunctionDef write_config(update_config, file_path)
**write_config**: The function of write_config is to update the existing configuration with new key-value pairs and write the updated configuration back to a file.

**parameters**:
- update_config: A dictionary containing the new key-value pairs to be added or updated in the configuration.
- file_path: An optional parameter representing the path to the configuration file. If not provided, the function will determine the file path internally.

**Code Description**:
The `write_config` function first checks if a file path is provided. If not, it calls the `get_config_path` function to determine the configuration file path. It then reads the existing configuration from the file, updates it with the new key-value pairs from `update_config`, and writes the modified configuration back to the file in TOML format.

The function ensures that the configuration file is loaded correctly and handles cases where the file might not exist or is empty. By updating the existing configuration with the new values, it allows for dynamic changes to the application's settings without losing previous configurations.

**Relationship with Callers**:
The `write_config` function is called by other parts of the project, such as the `configure` function in `main.py`, where it is used to save project and chat completion settings to the configuration file. Additionally, the `run` function in `main.py` invokes `write_config` to save the program settings before executing the main program logic.

**Note**:
- It is important to ensure that the `update_config` parameter is a dictionary containing valid key-value pairs.
- The function handles the file operations for configuration internally, simplifying the process for the caller.
- Any errors related to file handling or configuration updates are managed within the function to provide a smooth experience for the user.
