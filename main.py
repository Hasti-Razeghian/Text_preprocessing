from src.read_csv import read_csv

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
        if 'df' in locals():
            pass
        else:
            print("Please read a CSV file first.")
    elif choice == '3':
        if 'df' in locals():
            # output_directory = input("Enter the output directory for text files: ")
            # write_to_text_files(df, output_directory)
            pass
        else:
            print("Please read and preprocess the data first.")
    else:
        print("Invalid choice. Exiting program.")


main()
