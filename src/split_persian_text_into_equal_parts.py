def split_persian_text_into_equal_parts(text, n_parts):
    """
    Split a block of Persian text into a specified number of parts as evenly as possible,
    attempting to respect word boundaries.
    
    Parameters:
    - text (str): The Persian text to split.
    - n_parts (int): The number of parts to split the text into.
    
    Returns:
    - List[str]: A list of the text split into n_parts.
    """
    # Calculate the total length of the text and the approximate part size
    total_length = len(text)
    part_size = total_length // n_parts
    
    # Split the text into parts
    parts = []
    for i in range(n_parts):
        # For the last part, take all remaining text
        if i == n_parts - 1:
            parts.append(text)
            break
        
        # Find the nearest space to the dividing point to avoid splitting words
        split_point = text.rfind(' ', 0, part_size)
        
        # If we can't find a space (e.g., a very long word), split at the part size
        if split_point == -1:
            split_point = part_size
        
        parts.append(text[:split_point])
        
        # Update the text to remove the part we just added
        text = text[split_point:].lstrip()  # Remove leading spaces for the next part
    
    return parts

# Example usage
persian_text = "این یک متن نمونه برای تقسیم به چند بخش مساوی است. لطفاً این متن را به دقت تقسیم کنید تا هر بخش به طور مساوی توزیع شود."
n_parts = 3
parts = split_persian_text_into_equal_parts(persian_text, n_parts)

for i, part in enumerate(parts, start=1):
    print(f"Part {i}: {part}\n")
