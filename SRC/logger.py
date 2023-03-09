
'''
This code sets up logging in a Python script, which allows the script to output log messages to a file rather than to the console.

Here's what the code does:

1. It imports the logging and os modules, as well as the datetime class from the datetime module.
2. It creates a filename for the log file using the current date and time, and saves it in the LOG_FILE variable. The strftime() method of the datetime class is used to format the date and time in a specific way. For example, '%m_%d%Y_%H_%M_%S' would format the date and time as "03_09_2023_12_34_56".
3. It creates a logs_path variable that holds the full path to the directory where the log file will be stored. This path is constructed by joining the current working directory (returned by os.getcwd()) with a "logs" subdirectory and the LOG_FILE filename.
4. It creates the logs_path directory using os.makedirs() if it doesn't already exist. The exist_ok=True argument tells makedirs() to not raise an error if the directory already exists.
5. It creates the full path to the log file by joining the logs_path directory with the LOG_FILE filename, and saves it in the LOG_FILE_PATH variable.
6. It configures the logging module using the basicConfig() function. This function sets up some basic configuration for the logging module, such as where to write log messages, what format to use, and what level of messages to include.
7. The filename argument specifies the log file to write to, which is the LOG_FILE_PATH created in step 5.
8. The format argument specifies the format of the log messages. In this case, it includes the date and time, line number, logger name, log level, and message.
9. The level argument specifies the minimum log level to include in the log file. In this case, it's set to logging.INFO, which means only messages with a log level of INFO or higher will be included.

Once this code has been run, you can use the logging module to write log messages in your script using logging.info(), logging.warning(), logging.error(), and other methods. These messages will be written to the log file specified in LOG_FILE_PATH.

'''

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO,
)
