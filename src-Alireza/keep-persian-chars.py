import re

def keep_persian_chars(text):
    """Keep only Persian characters and numbers in the text."""
    # The range includes Persian letters and numbers
    persian_text = re.sub(r'[^\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF\u06F0-\u06F9 ]+', '', text)
    return persian_text
