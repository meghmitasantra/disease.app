import streamlit as st

st.set_page_config(page_title="About Us", layout="centered")

# ---------------- TEAM SECTION ----------------
st.markdown("""
<style>
            
.section {
    margin-top: 20px;   /* adds space before the text */
    padding: 10px;
}

/* Section container */
.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #1e3a5f;
    margin-top: 50px;
    margin-bottom: 20px;
    text-align: center;
}

/* Team grid */
.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 18px;
    margin-bottom: 40px;
}

/* Member card */
.member-card {
    background: linear-gradient(135deg, #ffffff, #f9fbff);
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.06);
    transition: 0.3s ease;
    text-align: center;
}

.member-card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 12px 25px rgba(0,0,0,0.12);
    border: 1px solid #3b82f6;
}

.member-name {
    font-size: 18px;
    font-weight: 600;
    color: #1e3a5f;
}

.member-role {
    font-size: 14px;
    color: #6b7280;
    margin-top: 6px;
}

/* Mentor card */
.mentor-card {
    background: linear-gradient(135deg, #1e3a5f, #3b82f6);
    padding: 30px;
    border-radius: 16px;
    color: white;
    text-align: center;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
}

.mentor-name {
    font-size: 22px;
    font-weight: 700;
}

.mentor-role {
    font-size: 15px;
    margin-top: 5px;
    opacity: 0.9;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TEAM ----------------
st.markdown('<div class="section-title">Team Members</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="member-card">
        <div class="member-name">Meghmita Santra</div>
        <div class="member-role">Machine Learning Algorithm</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="member-card">
        <div class="member-name">Labanya Mondal</div>
        <div class="member-role">Data Preprocessing</div>
    </div>
""", unsafe_allow_html=True)



st.markdown("""
    <div class="member-card">
        <div class="member-name">Salina Parvin</div>
        <div class="member-role">UI Designer</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="member-card">
        <div class="member-name">Soumi Ghosh</div>
        <div class="member-role">Data validation</div>
    </div>
""", unsafe_allow_html=True)
st.markdown("""
    <div class="member-card">
        <div class="member-name">Disha Kirtania</div>
        <div class="member-role">Data collection</div>
    </div>
""", unsafe_allow_html=True)

# ---------------- MENTOR ----------------
st.markdown('<div class="section-title">Project Mentor</div>', unsafe_allow_html=True)

st.markdown("""
<div class="mentor-card">
    <div class="mentor-name">Dr. Tapan Mondal</div>
    <div class="mentor-role">Assistant Professor & Project Guide</div>
</div>
""", unsafe_allow_html=True)

# ---------------- DESCRIPTION ----------------


st.markdown("""
<div class="section">
This project was developed as part of final year project to explore the application of 
machine learning in healthcare. The system demonstrates how predictive models can assist 
in identifying potential diseases using structured medical data.
</div>
""", unsafe_allow_html=True)

