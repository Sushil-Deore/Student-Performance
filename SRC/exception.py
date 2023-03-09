import sys # the sys module in python provides various functions and variables that are used to manipulate different parts of the python runtime environment
import logging
import logger

def error_massage_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info() # This gives execution info and this will give you three important information we are not interested in first and second, third will give location and error message
    
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_massage_detail(error_message, error_detail = error_detail)

    def __str__(self):
        return self.error_message

        