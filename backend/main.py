from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.ocr import extract_text
from backend.analyzer import analyze_health

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "File uploaded successfully", "file_path": file_path}


@app.get("/analyze/")
def analyze(file_path: str):
    try:
        text = extract_text(file_path)

        if not text:
            return {"error": "OCR failed to extract text"}

        result = analyze_health(text)

        return result

    except Exception as e:
        return {"error": str(e)}