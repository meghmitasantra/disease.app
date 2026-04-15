import streamlit as st
import numpy as np
import pickle
import sys

# Import custom model
from models.custom_models import RandomForestScratch, DecisionTreeNode

# Fix pickle loading
sys.modules['__main__'].RandomForestScratch = RandomForestScratch
sys.modules['__main__'].DecisionTreeNode = DecisionTreeNode

# Load model
with open("models/liver.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Liver Prediction", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background */
body {
    background-color: #f5f7fb;
}

/* Title */
.title {
    font-size: 36px;
    font-weight: 700;
    color: #1e3a5f;
    text-align: center;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #6b7280;
    margin-bottom: 30px;
}

/* Card */
.card {
    background: linear-gradient(135deg, #ffffff, #f9fbff);
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.06);
}

/* Button */
.stButton>button {
    background: linear-gradient(135deg, #1e3a5f, #3b82f6);
    color: white;
    border-radius: 10px;
    padding: 10px 25px;
    font-weight: 600;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 8px 20px rgba(0,0,0,0.2);
}

/* Result */
.result-box {
    margin-top: 20px;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
}

.success {
    background-color: #e6f4ea;
    color: #1b5e20;
}

.error {
    background-color: #fdecea;
    color: #b71c1c;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">Liver Disease Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter biochemical parameters to assess liver health</div>', unsafe_allow_html=True)

# ---------------- INPUT CARD ----------------


col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 40)
    gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0,1])
    total_bilirubin = st.number_input("Total Bilirubin", 0.0, 10.0, 1.0)
    direct_bilirubin = st.number_input("Direct Bilirubin", 0.0, 5.0, 0.3)
    alkphos = st.number_input("Alkaline Phosphotase", 50.0, 1000.0, 200.0)

with col2:
    sgpt = st.number_input("SGPT (ALT)", 0.0, 500.0, 30.0)
    sgot = st.number_input("SGOT (AST)", 0.0, 500.0, 30.0)
    total_proteins = st.number_input("Total Proteins", 2.0, 10.0, 6.0)
    albumin = st.number_input("Albumin", 1.0, 6.0, 3.0)
    ag_ratio = st.number_input("A/G Ratio", 0.0, 2.5, 1.0)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if st.button("Predict"):

    input_data = np.array([[
        age,
        gender,
        total_bilirubin,
        direct_bilirubin,
        alkphos,
        sgpt,
        sgot,
        total_proteins,
        albumin,
        ag_ratio
    ]])

    prediction = model.predict(input_data)

    # ---------------- RESULT ----------------
    # ⚠️ Handle dataset labels (1 = disease, 2 = healthy OR 0 = healthy)
    if prediction[0] == 1:
        st.markdown('<div class="result-box error">Liver Disease Detected</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box success">Healthy Liver</div>', unsafe_allow_html=True)

