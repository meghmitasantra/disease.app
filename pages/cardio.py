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
with open("models/cardio.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Cardio Prediction", layout="centered")

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
st.markdown('<div class="title">Cardiovascular Disease Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter clinical parameters to assess heart disease risk</div>', unsafe_allow_html=True)



col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 30)
    gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0, 1])
    chestpain = st.selectbox("Chest Pain Type (0–3)", [0,1,2,3])
    resting_bp = st.number_input("Resting Blood Pressure", 80, 250, 120)
    chol = st.number_input("Serum Cholesterol", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 (0 = No, 1 = Yes)", [0,1])

with col2:
    restecg = st.selectbox("Resting ECG (0–2)", [0,1,2])
    max_hr = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
    ex_angina = st.selectbox("Exercise Induced Angina (0 = No, 1 = Yes)", [0,1])
    oldpeak = st.number_input("Oldpeak (ST Depression)", 0.0, 10.0, 1.0)
    slope = st.selectbox("Slope (1–3)", [1,2,3])
    vessels = st.selectbox("No. of Major Vessels (0–3)", [0,1,2,3])

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if st.button("Predict"):

    input_data = np.array([[
        age,
        gender,
        chestpain,
        resting_bp,
        chol,
        fbs,
        restecg,
        max_hr,
        ex_angina,
        oldpeak,
        slope,
        vessels
    ]])

    prediction = model.predict(input_data)

    # ---------------- RESULT ----------------
    if prediction[0] == 1:
        st.markdown('<div class="result-box error">Heart Disease Detected</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box success">Healthy - No Heart Disease</div>', unsafe_allow_html=True)


