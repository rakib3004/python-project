import os
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def reduce_pdf_size(input_path, output_path, compression=0):
    try:
        # Read the input PDF
        reader = PdfReader(input_path)

        # Create an output PDF writer
        pdf_writer = PdfWriter()

        # Iterate through each page and add it to the output PDF
        for page_num in range(len(reader.pages)):
            output_page = pdf_writer.add_page(reader.pages[page_num])
            output_page.compress_content(compression)

        # Save the output PDF to a BytesIO buffer
        output_buffer = BytesIO()
        pdf_writer.write(output_buffer)
        output_buffer.seek(0)

        # Create a canvas for the output PDF
        output_canvas = canvas.Canvas(output_path, pagesize=letter)
        output_canvas.drawString(100, 100, "Reduced PDF using ReportLab")
        output_canvas.save()

        # Merge the compressed content and the canvas
        with open(output_path, 'wb') as output_file:
            output_file.write(output_buffer.read())

        print(f"Reduced file: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def process_pdf_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, "reduced_" + filename)
            reduce_pdf_size(input_path, output_path)

if __name__ == "__main__":
    target_folder = r"D:\ObjectOrientedConcepts2Slides"  # Replace with your folder path
    process_pdf_folder(target_folder)
