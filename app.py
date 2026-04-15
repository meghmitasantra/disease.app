import streamlit as st

st.set_page_config(page_title="Disease Prediction System", layout="wide")

# ---------------- ANIMATED CSS ----------------
st.markdown("""
<style>

/* -------- ANIMATIONS -------- */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* -------- BACKGROUND -------- */
body {
    background: linear-gradient(-45deg, #f4f6fb, #eef2ff, #f8fafc, #e0f2fe);
    background-size: 400% 400%;
    animation: gradientMove 12s ease infinite;
}

/* -------- HEADER -------- */
.main-title {
    font-size: 50px;
    font-weight: 800;
    text-align: center;
    color: #1e3a5f;
    animation: fadeIn 1s ease-in-out;
}

.subtitle {
    text-align: center;
    color: #6b7280;
    margin-bottom: 40px;
    animation: fadeIn 1.5s ease-in-out;
}

/* -------- FEATURE BOX -------- */
.feature-bar {
    display: flex;
    justify-content: space-around;
    margin-bottom: 40px;
}

.feature-box {
    background: white;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    width: 22%;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    transition: 0.3s;
    animation: fadeIn 2s ease;
}

.feature-box:hover {
    transform: translateY(-6px) scale(1.03);
}

/* -------- CARD -------- */
.card {
    background: linear-gradient(135deg, #ffffff, #f9fbff);
    padding: 28px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.06);
    transition: all 0.4s ease;
    animation: fadeIn 2.5s ease;
    position: relative;
    overflow: hidden;

    min-height: 130px;  /* ✅ ADD THIS */
    
}

/* Glow animation */
.card::before {
    content: "";
    position: absolute;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(59,130,246,0.15), transparent 70%);
    top: -50%;
    left: -50%;
    opacity: 0;
    transition: 0.4s;
}

.card:hover::before {
    opacity: 1;
}

.card:hover {
    transform: translateY(-10px) scale(1.03);
    box-shadow: 0px 14px 35px rgba(0,0,0,0.2);
    border: 1px solid #3b82f6;
}

/* -------- TEXT -------- */
.card-title {
    font-size: 22px;
    font-weight: 600;
    color: #1e3a5f;
}

.card-text {
    font-size: 15px;
    color: #4b5563;
    margin-top: 10px;
}

/* -------- ABOUT -------- */
.about {
    background: linear-gradient(135deg, #1e3a5f, #3b82f6);
    padding: 50px;
    border-radius: 18px;
    color: white;
    text-align: center;
    margin-top: 50px;
    animation: fadeIn 3s ease;
}

/* -------- FOOTER -------- */
.footer {
    text-align: center;
    margin-top: 40px;
    color: gray;
    animation: fadeIn 3.5s ease;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">Disease Prediction System</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">AI-powered healthcare platform for early disease detection</div>',
    unsafe_allow_html=True
)

# ---------------- FEATURES ----------------
st.markdown("""
<div class="feature-bar">
    <div class="feature-box"><b>5 Models</b><br>Multi-disease system</div>
    <div class="feature-box"><b>AI Powered</b><br>Custom ML models</div>
    <div class="feature-box"><b>Fast</b><br>Instant prediction</div>
    <div class="feature-box"><b>Reliable</b><br>Accurate outputs</div>
</div>
""", unsafe_allow_html=True)

# ---------------- CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">Asthma Prediction</div>
        <div class="card-text">Respiratory symptom-based analysis for asthma detection.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Alzheimer Prediction</div>
        <div class="card-text">Cognitive and lifestyle-based prediction system.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">Cardiovascular Disease</div>
        <div class="card-text">Heart condition analysis using clinical parameters.</div>
    </div>
    """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
        <div class="card-title">Diabetes Prediction</div>
        <div class="card-text">Glucose, BMI, and health indicators based prediction.</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <div class="card-title">Liver Disease Prediction</div>
        <div class="card-text">Biochemical marker-based liver health detection.</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <div class="card-title">Navigation</div>
        <div class="card-text">Use sidebar to access prediction modules.</div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- ABOUT ----------------
st.markdown("""
<div class="about">
    <h2>About the Platform</h2>
    This system integrates multiple machine learning models to provide early disease detection. 
    Designed for research and educational use, it demonstrates how AI can assist in healthcare analytics.
</div>
""", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown('<div class="footer">Machine Learning Healthcare System</div>', unsafe_allow_html=True)


