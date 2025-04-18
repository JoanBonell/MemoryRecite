# src/pdf_processing/pdf_extractor.py
import PyPDF2
from io import StringIO
from pdfminer.high_level import extract_text


def extract_text_pypdf2(file_path: str) -> str:
    """
    Extrae texto de un PDF utilizando PyPDF2.
    Retorna el texto en formato string.
    """
    text_content = []
    try:
        with open(file_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page in pdf_reader.pages:
                text_content.append(page.extract_text())
        return "\n".join(text_content)
    except Exception as e:
        print(f"Error en extract_text_pypdf2: {e}")
        return ""


def extract_text_pdfminer(file_path: str) -> str:
    """
    Extrae texto de un PDF utilizando pdfminer.
    Retorna el texto en formato string.
    """
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        print(f"Error en extract_text_pdfminer: {e}")
        return ""


def extract_text_unified(file_path: str) -> str:
    """
    Combina ambos métodos (PyPDF2 y pdfminer) para tener mayor
    robustez en la extracción. Si uno falla o extrae poco texto,
    intenta con el otro.
    """
    text_pypdf2 = extract_text_pypdf2(file_path)
    # Validamos si PyPDF2 extrajo algo
    if len(text_pypdf2.strip()) > 50:  # si extrajo más de 50 caracteres
        return text_pypdf2
    else:
        # Si PyPDF2 no funcionó bien, probamos con pdfminer
        text_pdfminer = extract_text_pdfminer(file_path)
        return text_pdfminer
