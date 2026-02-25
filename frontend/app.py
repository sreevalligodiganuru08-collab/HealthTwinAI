import streamlit as st
import requests

st.title("HealthTwin AI 🧠")

uploaded_file = st.file_uploader("Upload Health Report", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

    if st.button("Analyze Report"):
        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            "http://127.0.0.1:8000/upload-report",
            files={"file": (uploaded_file.name, uploaded_file.getvalue())}
        )

        if response.status_code == 200:
            data = response.json()
            st.write("### Result")
            st.write(data)
        else:
            st.error("Error in processing")