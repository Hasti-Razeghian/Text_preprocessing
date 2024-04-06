import re

"""Takes a string and remove url"""


def remove_url(text):
    return re.sub(r'http\S+', '', text)