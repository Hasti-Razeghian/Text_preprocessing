def remove_punctuation(data: str):

    """ Takes a string and remove its punctuations """

    unwanted_punc = ['.',',',':','!','?',';']
    for punc in unwanted_punc:
        data = data.replace(punc, "")

    return data

