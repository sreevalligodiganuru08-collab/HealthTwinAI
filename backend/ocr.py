from PIL import Image
import pytesseract
import io
import pdfplumber


# Set path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(file_bytes):
    text = ""

    try:
        # Try as image
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image)

    except:
        try:
            # Try as PDF
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        except:
            text = "Unable to extract text"

    return text