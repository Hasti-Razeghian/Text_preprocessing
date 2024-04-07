from src.read_csv import read_csv
from src.remove_special_char import remove_special_char
from src.remove_newline_tab import remove_newline_tab
from src.convert_lowercase import convert_lowercase
from src.remove_punctuation import remove_punctuation
from src.remove_whitespace import remove_whitespace
from src.remove_url import remove_url
from src.remove_html_tags import remove_html_tags
from src.remove_digits import remove_digits
from src.remove_stop_words_persian import remove_stop_words_persian
from src.reduce_repeated_chars import reduce_repeated_chars
from src.remove_unicode_chars import remove_unicode_chars
from src.change_font_and_size import change_font_and_size
from src.split_persian_text_into_equal_parts import split_persian_text_into_equal_parts
from src.write_sections_to_files import write_sections_to_files
from src.write_sections_to_files import divide_into_sections



def main():
    print("Menu:")
    print("1. Read CSV file")
    print("2. Preprocess data")
    print("3. Write to text files")
    print("Please enter the number corresponding to the action you want to perform.")
   
    choice = input("Enter your choice (1-3): ")
   
    if choice == '1':
        data = read_csv(r'data/INFO.csv',6)
        print(data.head())

    elif choice == '2':
        if 'data' in locals():
            clean_data = remove_special_char(data)
            clean_data = remove_newline_tab(data)
            clean_data = convert_lowercase(data)
            clean_data = remove_punctuation(data)
            clean_data = remove_whitespace(data)
            clean_data = remove_url(data)
            clean_data = remove_html_tags(data)
            clean_data = remove_digits(data)
            clean_data = remove_stop_words_persian(data)
            clean_data = reduce_repeated_chars(data)
            lean_data = remove_unicode_chars(data)
            clean_data = change_font_and_size (data)
            clean_data = split_persian_text_into_equal_parts (data)
        else:
            print("Please read a CSV file first.")
    elif choice == '3':
        if 'data' in locals():
            # output_directory = input("Enter the output directory for text files: ")
            # write_to_text_files(df, output_directory)
            clean_data = divide_into_sections(data)
            clean_data = write_sections_to_files (data)
        else:
            print("Please read and preprocess the data first.")
    else:
        print("Invalid choice. Exiting program.")


main()
