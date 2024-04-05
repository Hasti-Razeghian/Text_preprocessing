import re

def remove_whitespace(data:str):

    """Takes a string and remove extra whitespaces"""

    clean_data = re.sub(re.compile(r'\s+'), " ", data)

    return clean_data

