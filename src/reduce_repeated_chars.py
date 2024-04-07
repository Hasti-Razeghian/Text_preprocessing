import re

def reduce_repeated_chars(text, max_repeats=2):
    """
    Reduces repeated characters in a string to a maximum specified number.
    
    Parameters:
    - text (str): The text to process.
    - max_repeats (int): The maximum number of times a character may be repeated.
    
    Returns:
    - str: The processed text with reduced character repetitions.
    """
    pattern = r'(.)\1{' + str(max_repeats) + ',}'
    reduced_text = re.sub(pattern, r'\1' * max_repeats, text)
    return reduced_text

# Example usage:
sample_text = "سلامممممم! چطوووورییییی؟؟؟"
reduced_text = reduce_repeated_chars(sample_text)
print("Original Text:", sample_text)
print("Reduced Text:", reduced_text)
