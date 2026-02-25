import re


def extract_value(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    return float(match.group(1)) if match else None


def analyze_health(text):
    
    hemoglobin = extract_value(r"hemoglobin[:\s]*([\d.]+)", text)
    glucose = extract_value(r"glucose[:\s]*([\d.]+)", text)

    # Default fallback
    if hemoglobin is None:
        hemoglobin = 11.5
    if glucose is None:
        glucose = 120

    score = 100

    if hemoglobin < 11:
        score -= 20

    if glucose > 130:
        score -= 20

    if score > 80:
        risk = "Low"
    elif score > 60:
        risk = "Moderate"
    else:
        risk = "High"

    explanation = f"Hemoglobin: {hemoglobin}, Glucose: {glucose}"

    return score, risk, explanation