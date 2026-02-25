# HealthTwinAI
AI HealthTwin: Universal Report Analyzer + Preventive Health System
## Setup Instructions

### Backend
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload

### Frontend
cd frontend
pip install streamlit requests
python -m streamlit run app.py

### API Docs
http://127.0.0.1:8000/docs