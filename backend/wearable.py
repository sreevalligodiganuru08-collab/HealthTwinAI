import random

def get_wearable_data():
    return {
        "heart_rate": random.randint(70, 100),
        "spo2": random.randint(93, 99),
        "temperature": round(random.uniform(97, 100), 1),
        "steps": random.randint(1000, 5000),
        "sleep_hours": random.randint(4, 8)
    }