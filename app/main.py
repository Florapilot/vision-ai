
import streamlit as st
from PIL import Image

st.set_page_config(page_title="FloraPilot - Flower Grading")

st.title("🌸 FloraPilot Vision AI Demo")

uploaded_file = st.file_uploader("Upload a flower image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.success("Predicted Grade: Export-Quality 🌼 (Simulated)")
    st.info("Confidence: 92.5%")
