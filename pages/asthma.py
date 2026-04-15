import streamlit as st
import numpy as np
import pickle
import sys

# Import custom model module
import models.custom_models as cm

# Fix pickle loading
for name in dir(cm):
    setattr(sys.modules['__main__'], name, getattr(cm, name))

# Load model
with open("models/asthma.pkl", "rb") as f:
    model = pickle.load(f)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Asthma Prediction", layout="centered")

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
st.markdown('<div class="title">Asthma Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter patient respiratory details for prediction</div>', unsafe_allow_html=True)



col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 0, 120, 30)
    gender = st.number_input("Gender (0 = Female, 1 = Male)", 0, 1, 0)
    smoking = st.number_input("Smoking (0 = No, 1 = Yes)", 0, 1, 0)
    petallergy = st.number_input("Pet Allergy (0 = No, 1 = Yes)", 0, 1, 0)
    familyhistory = st.number_input("Family History (0 = No, 1 = Yes)", 0, 1, 0)

with col2:
    breath = st.number_input("Shortness of Breath", 0, 1, 0)
    chest = st.number_input("Chest Tightness", 0, 1, 0)
    cough = st.number_input("Coughing", 0, 1, 0)
    night = st.number_input("Night Symptoms", 0, 1, 0)
    exercise = st.number_input("Exercise Induced", 0, 1, 0)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
if st.button("Predict"):

    input_data = np.array([[
        age,
        gender,
        smoking,
        petallergy,
        familyhistory,
        breath,
        chest,
        cough,
        night,
        exercise
    ]])

    prediction = model.predict(input_data)

    # ---------------- RESULT ----------------
    if prediction[0] == 1:
        st.markdown('<div class="result-box error">Asthma Detected</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box success">No Asthma Detected</div>', unsafe_allow_html=True)

