import re

"""Takes a string and remove url"""


def remove_url(data:str):
    return re.sub(r'https?://[a-zA-Z0-9\.\/-_?=;&]*', '', data)