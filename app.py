import streamlit as st
import requests

st.title("🧠 HealthTwin AI")

uploaded_file = st.file_uploader("Upload Medical Report", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    if st.button("Analyze"):
        
        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            "http://127.0.0.1:8000/upload-report",
            files={"file": uploaded_file}
        )

        if response.status_code == 200:
            data = response.json()

            st.success(f"Risk Level: {data['risk']}")
            st.metric("Health Score", data["score"])
            st.write(data["explanation"])
        else:
            st.error("Something went wrong")