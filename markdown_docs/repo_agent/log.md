## ClassDef InterceptHandler
**InterceptHandler**: The function of InterceptHandler is to intercept standard logging messages and redirect them to Loguru for processing.

**attributes**:
- None

**Code Description**:
InterceptHandler is a class that extends the logging.Handler class. It overrides the emit method to intercept standard logging messages and redirect them to Loguru for logging. The emit method retrieves the log level, finds the origin of the logged message, and then logs the message using Loguru.

In the calling situation within the project, the InterceptHandler class is utilized in the set_logger_level_from_config function in the log.py file. In this function, the InterceptHandler class is added as a handler to the root logger to intercept standard logging messages and redirect them to Loguru. This allows for setting the log level and handling log messages effectively.

**Note**:
Developers can use the InterceptHandler class to customize the handling of log messages and integrate standard logging with Loguru seamlessly.
### FunctionDef emit(self, record)
**emit**: The function of emit is to log a record using Loguru based on the provided record.

**parameters**:
- self: The instance of the class.
- record: The log record to be emitted.

**Code Description**:
The emit function first attempts to determine the corresponding Loguru level based on the record's level name. If a ValueError occurs, it uses the record's level number instead. 

Next, it iterates through the call stack to find the origin of the logged message. It does this by checking the filename of the frame until it reaches a different file.

Finally, the function logs the message to Loguru using the determined level and the message extracted from the record.

**Note**:
- This function is designed to be used within a logging system that utilizes Loguru.
- It handles exceptions when determining the log level and finding the caller's location.
***
## FunctionDef set_logger_level_from_config(log_level)
**set_logger_level_from_config**: The function of set_logger_level_from_config is to set the logger level for logging and intercept standard logging messages, redirecting them to Loguru for processing.

**parameters**:
- log_level: The desired log level to be set for logging.

**Code Description**:
The set_logger_level_from_config function removes the existing logger, adds a new logger with the specified log level, intercepts standard logging messages, and redirects them to Loguru for processing. It sets the log level and displays a success message indicating the log level has been updated.

In the project, this function is called within the run function in main.py. It is invoked to set the logger level based on the configuration provided in the project settings. By utilizing the InterceptHandler class, standard logging messages are intercepted and redirected to Loguru, ensuring effective handling of log messages.

**Note**:
Developers can use set_logger_level_from_config to dynamically adjust the log level and seamlessly integrate standard logging with Loguru for efficient logging and monitoring of the application.
