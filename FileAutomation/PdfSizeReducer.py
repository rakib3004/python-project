import os
import fitz  # PyMuPDF


def reduce_pdf_size(input_path, output_path, quality=50):
    try:
        # Open the input PDF file
        pdf_document = fitz.open(input_path)

        # Initialize the output PDF document
        pdf_document_resized = fitz.open()

        # Iterate through all pages and copy them with reduced quality to the new document
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            new_page = pdf_document_resized.new_page(width=page.width, height=page.height)
            new_page.show_pdf_page(page)

        # Save the new PDF with reduced size
        pdf_document_resized.save(output_path, deflate=True, quality=quality)

        # Close the documents
        pdf_document.close()
        pdf_document_resized.close()

        print(f"Reduced file: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Error: {e}")


def process_pdf_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, "resized_" + filename)
            reduce_pdf_size(input_path, output_path)

            # Replace the original file with the resized one
            os.remove(input_path)
            os.rename(output_path, input_path)


if __name__ == "__main__":
    target_folder = r"C:\path\to\your\folder"  # Replace with your folder path
    process_pdf_folder(target_folder)
