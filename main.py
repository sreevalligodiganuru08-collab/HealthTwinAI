from fastapi import FastAPI, File, UploadFile
from ocr import extract_text
from analyzer import analyze_health
import io

app = FastAPI()


@app.get("/")
def home():
    return {"message": "HealthTwin AI Backend Running 🚀"}


@app.post("/upload-report")
async def upload_report(file: UploadFile = File(...)):
    
    # Read file
    contents = await file.read()

    # Step 1: OCR
    text = extract_text(contents)

    # Step 2: Analysis
    score, risk, explanation = analyze_health(text)

    return {
        "score": score,
        "risk": risk,
        "explanation": explanation
    }