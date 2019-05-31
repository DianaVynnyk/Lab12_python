import re

import logging

def getFile():
    logger = logging.getLogger(__name__)
    f_handler = logging.FileHandler('file.log')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)
    logger.addHandler(f_handler)
    logger.error('This is an error')