def remove_special_char(data:str):

    """ Takes a string and removes its special characters """

    unwanted_punc = ['"',"'",'=','@','&','%','\\','$','^','<','>','{','}',';','\n','\t','(',')','[',']','/','*','+','#','\u200c','\ufeff','-','_','|']

    for punc in unwanted_punc:
        data = data.replace(punc, "")

    return data


    