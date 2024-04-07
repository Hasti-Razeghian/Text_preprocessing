import pandas as pd

# def read_last_column(csv_file_path):
#     """Read the last column of a CSV file."""
#     df = pd.read_csv(csv_file_path)
#     return df.iloc[:, -1]

def divide_into_sections(column_data):
    """Divide a pandas Series into 3 equal parts."""
    total_length = len(column_data)
    section_length = total_length // 3
    sections = [
        column_data.iloc[:section_length],
        column_data.iloc[section_length:2*section_length],
        column_data.iloc[2*section_length:]
    ]
    return sections

def write_sections_to_files(sections, base_filepath="/mnt/data/section"):
    """Write each section to a separate text file."""
    for i, section in enumerate(sections, start=1):
        filename = f"{base_filepath}_{i}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            for item in section:
                file.write(f"{item}\n")
        print(f"Section {i} written to {filename}")

# Example usage:
csv_file_path = 'path_to_your_file/INFO.csv'  # Make sure to update this path
# last_column = read_last_column(csv_file_path)
sections = divide_into_sections(csv_file_path)
write_sections_to_files(sections)
