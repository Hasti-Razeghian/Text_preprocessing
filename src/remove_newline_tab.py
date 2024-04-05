def remove_newline_tab(data:str):

    """ Takes a string and removes every newlines and tabs """

    clean_data = data.replace("\\n", " ") # remove new lines \n
    clean_data = clean_data.replace("\\t", " ") # remove tabs \t

    return clean_data

