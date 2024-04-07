"""This function change size and font"""
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_pdf_from_csv(csv_file_path, output_folder, font_path="PersianFont.ttf", font_size=12):
    # Read the CSV file and get the last column
    df = pd.read_csv(csv_file_path)
    last_column = df.iloc[:, -1]
   
    for index, text in enumerate(last_column, start=1):
        # Create a PDF file for each row
        c = canvas.Canvas(f"{output_folder}/output_{index}.pdf", pagesize=letter)
        c.setFont("Helvetica", font_size)  # Set a default font and size
       
        # Register a Persian-compatible font
        c.registerFont("PersianFont", font_path)
        c.setFont("PersianFont", font_size)
       
        # Add the text to the PDF
        c.drawString(100, 750, text)  # Adjust position as needed
       
        # Save the PDF
        c.save()
       
    print(f"PDFs have been created in {output_folder}.")

# Example usage
csv_file_path = 'path_to_your_file.csv'  # Update this path to your CSV file
output_folder = 'path_to_output_folder'  # Update this to your desired output folder
font_path = 'path_to_your_font/PersianFont.ttf'  # Update this path to your font file

create_pdf_from_csv(csv_file_path, output_folder, font_path, font_size=12)