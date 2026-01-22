
import pypdf
import sys

def extract_one(pdf_path, out_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = f"# Document: {pdf_path}

"
        for page in reader.pages:
            text += page.extract_text() + "
"
        
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"Error: {e}")

if __name__ == "__main__":
    extract_one("62451.pdf", "debug_62451.txt")
