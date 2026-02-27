from backend.predictor import predict_risk

def analyze_health(text, wearable_data):
    
    # Temporary fixed values (can upgrade later)
    hemoglobin = 11.5
    glucose = 120

    # Get prediction from wearable data
    score, risk = predict_risk(wearable_data, [])

    explanation = f"""
    Hemoglobin: {hemoglobin}
    Glucose: {glucose}
    Heart Rate: {wearable_data['heart_rate']}
    SpO2: {wearable_data['spo2']}
    Sleep: {wearable_data['sleep_hours']}
    """

    return score, risk, explanation