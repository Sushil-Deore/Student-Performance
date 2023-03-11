import os
import sys
import numpy as np
import pandas as pd
import dill

from SRC.exception import CustomException
from SRC.logger import logging

def save_object(file_path, obj):
    logging.info("Entering Save_object")
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        
        
        logging.info('Dumping is done in save object')

    except Exception as e:
        raise CustomException(e, sys)