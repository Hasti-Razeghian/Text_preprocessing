import re

def clean_persian_text(text):
    """
    Remove unwanted Unicode characters from a Persian text string, 
    keeping Persian letters, numerals, and basic punctuation.
    """
    # Regex pattern: includes Persian letters, Arabic-Indic numerals, and basic punctuation
    pattern = r'[^ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیئًٌٍَُِّْٔ۰۱۲۳۴۵۶۷۸۹\s،؛؟.!]'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

# Example usage:
sample_text = "این یک متن فارسی است با برخی کاراکترهای غیرمعمولی: [abc] {123} 🎉"
cleaned_text = clean_persian_text(sample_text)
print("Cleaned Text:", cleaned_text)
