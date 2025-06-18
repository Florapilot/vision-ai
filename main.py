
import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="FloraPilot - Flower Grading AI")

st.title("FloraPilot Vision AI - Flower Grading Demo")

uploaded_file = st.file_uploader("Upload a flower image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("✅ Simulated Grade: Export-quality 🌸")
    st.write("Confidence Score: 92.5%")

st.markdown("Note: This is a mockup using placeholder results. Model coming soon.")
