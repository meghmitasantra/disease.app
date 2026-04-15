import streamlit as st
import joblib

def load_model(path):
    return joblib.load(path)   # ✅ works for .pkl also

def apply_style():
    st.markdown("""
    <style>
    .main { background-color: #f4f6f9; }
    .title {
        font-size: 32px;
        font-weight: bold;
        color: #1f4e79;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)