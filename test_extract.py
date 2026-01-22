
import pypdf
import sys

def extract_text(pdf_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "
"
        return text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(extract_text("62451.pdf"))
