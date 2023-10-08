import PyPDF2

def get_content(file_path):
    try:
        pdf_reader = PyPDF2.PdfReader(file_path)

        num_pages = len(pdf_reader.pages)
        pdf_content = "File preview"

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_content += page.extract_text() + "\n"

        return pdf_content

    except Exception as e:
        print(e)