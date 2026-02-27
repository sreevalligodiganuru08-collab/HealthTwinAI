def predict_risk(wearable, history):
    
    hr = wearable["heart_rate"]
    spo2 = wearable["spo2"]
    sleep = wearable["sleep_hours"]

    risk_score = 100

    if hr > 90:
        risk_score -= 20
    if spo2 < 95:
        risk_score -= 20
    if sleep < 5:
        risk_score -= 10

    if risk_score > 80:
        risk = "Low"
    elif risk_score > 60:
        risk = "Moderate"
    else:
        risk = "High"

    return risk_score, risk