def correct_typos_persian(text, typo_dict):
    """
    Correct typos in Persian text based on a predefined dictionary of common typos.

    Parameters:
    - text (str): The text to be corrected.
    - typo_dict (dict): A dictionary where keys are common typos and values are the correct forms.

    Returns:
    - str: The corrected text.
    """
    for typo, correct in typo_dict.items():
        text = text.replace(typo, correct)
    return text

# Example usage:
typo_dict = {
    "سللم": "سلام",  # Hello
    "خخوبی": "خوبی",  # How are you
    # Add more common typos and corrections here
}

sample_text = "سللم! خخوبی؟"
corrected_text = correct_typos_persian(sample_text, typo_dict)
print("Corrected Text:", corrected_text)
