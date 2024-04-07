from nltk.tokenize import word_tokenize

# Example list of Persian stop words, you should expand this list
persian_stop_words = ['و', 'در', 'به', 'از', 'که']

def remove_stop_words_persian(text):
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in persian_stop_words]
    filtered_text = ' '.join(filtered_text)
    return filtered_text
