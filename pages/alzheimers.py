import streamlit as st
import numpy as np
import pickle
import sys

from models.custom_models import RandomForestScratch, DecisionTreeNode

# Fix pickle issue
sys.modules['__main__'].RandomForestScratch = RandomForestScratch
sys.modules['__main__'].DecisionTreeNode = DecisionTreeNode

# Load model
with open("models/alzheimer.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Alzheimer Prediction", layout="centered")

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

/* Result box */
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
st.markdown('<div class="title">Alzheimer Disease Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter patient details to assess Alzheimer risk</div>', unsafe_allow_html=True)



col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 50)
    gender = st.selectbox("Gender (0 = Female, 1 = Male)", [0,1])
    bmi = st.number_input("BMI", 10.0, 50.0, 22.0)
    activity = st.number_input("Physical Activity Score", 0.0, 10.0, 5.0)
    diet = st.number_input("Diet Quality Score", 0.0, 10.0, 5.0)

with col2:
    sleep = st.number_input("Sleep Quality Score", 0.0, 10.0, 5.0)
    family = st.selectbox("Family History (0 = No, 1 = Yes)", [0,1])
    diabetes = st.selectbox("Diabetes (0 = No, 1 = Yes)", [0,1])
    depression = st.selectbox("Depression (0 = No, 1 = Yes)", [0,1])

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if st.button("Predict"):

    input_data = np.array([[
        age,
        gender,
        bmi,
        activity,
        diet,
        sleep,
        family,
        diabetes,
        depression
    ]])

    prediction = model.predict(input_data)

    # ---------------- RESULT ----------------
    if prediction[0] == 1:
        st.markdown('<div class="result-box error">High Risk of Alzheimer Detected</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box success">Low Risk / No Alzheimer Detected</div>', unsafe_allow_html=True)


