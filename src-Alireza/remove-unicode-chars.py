import re

def remove_unicode_chars(text):
    """Remove Unicode characters from a string, leaving only ASCII characters."""
    ascii_text = re.sub(r'[^\x00-\x7F]+', '', text)
    return ascii_text

# Example usage:
sample_text = "Hello, world! 👋🌍"
clean_text = remove_unicode_chars(sample_text)
print("Original Text:", sample_text)
print("Cleaned Text:", clean_text)