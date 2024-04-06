import re

"""Takes a string and remove html_tags"""



def remove_html_tags(data:str):
    return re.sub(r'<[^>]+>', '', data)
