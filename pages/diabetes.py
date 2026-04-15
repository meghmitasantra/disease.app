import streamlit as st
import numpy as np
import pickle
import sys

# Import custom model
from models.custom_models import RandomForestScratch, DecisionTreeNode

# Fix pickle issue
sys.modules['__main__'].RandomForestScratch = RandomForestScratch
sys.modules['__main__'].DecisionTreeNode = DecisionTreeNode

# Load model
with open("models/diabetes.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Diabetes Prediction", layout="centered")

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
st.markdown('<div class="title">Diabetes Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter patient health parameters to assess diabetes risk</div>', unsafe_allow_html=True)



col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 40)
    gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0,1])
    pulse = st.number_input("Pulse Rate", 40, 150, 80)
    sys_bp = st.number_input("Systolic BP", 80, 250, 120)
    dia_bp = st.number_input("Diastolic BP", 40, 150, 80)
    glucose = st.number_input("Glucose Level", 0.0, 20.0, 5.5)
    height = st.number_input("Height (meters)", 1.0, 2.5, 1.6)

with col2:
    weight = st.number_input("Weight (kg)", 20.0, 200.0, 60.0)
    bmi = st.number_input("BMI", 10.0, 50.0, 22.0)
    family_diabetes = st.selectbox("Family Diabetes (0 = No, 1 = Yes)", [0,1])
    hypertensive = st.selectbox("Hypertensive (0 = No, 1 = Yes)", [0,1])
    family_hyper = st.selectbox("Family Hypertension (0 = No, 1 = Yes)", [0,1])
    cardio = st.selectbox("Cardiovascular Disease (0 = No, 1 = Yes)", [0,1])
    stroke = st.selectbox("Stroke History (0 = No, 1 = Yes)", [0,1])

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if st.button("Predict"):

    input_data = np.array([[
        age,
        gender,
        pulse,
        sys_bp,
        dia_bp,
        glucose,
        height,
        weight,
        bmi,
        family_diabetes,
        hypertensive,
        family_hyper,
        cardio,
        stroke
    ]])

    prediction = model.predict(input_data)

    # ---------------- RESULT ----------------
    if prediction[0] == 1:
        st.markdown('<div class="result-box error">Diabetes Detected</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box success">No Diabetes Detected</div>', unsafe_allow_html=True)


