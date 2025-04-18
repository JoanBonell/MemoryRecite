# tests/test_pdf_extractor.py

import os
from src.pdf_processing.pdf_extractor import extract_text_unified

def test_pdf_extraction():
    pdf_path = os.path.join("data", "documento_prueba.pdf")
    extracted_text = extract_text_unified(pdf_path)
    print("Texto extraído:\n", extracted_text)

if __name__ == "__main__":
    test_pdf_extraction()

# Para ejecutar este test:
#python .\tests\test_pdf_extractor.py