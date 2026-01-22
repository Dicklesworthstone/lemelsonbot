# /// script
# dependencies = ["pypdf"]
# ///

from pypdf import PdfReader
import sys

try:
    reader = PdfReader("62451.pdf")
    with open("output_test.txt", "w") as f:
        # Extract text from the first 5 pages to get a sense of metadata
        for i in range(min(5, len(reader.pages))):
            page = reader.pages[i]
            text = page.extract_text()
            f.write(f"--- Page {i+1} ---
")
            f.write(text)
            f.write("

")
    print("Extraction complete.")
except Exception as e:
    with open("output_test.txt", "w") as f:
        f.write(f"Error: {e}")
