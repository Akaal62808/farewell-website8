import streamlit as st

st.set_page_config(page_title="Farewell Mam", layout="centered")

# Background & Styling
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
}

.big-title {
    font-size: 55px;
    text-align: center;
    color: #ff0066;
    font-weight: bold;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #ff99cc; }
    to { text-shadow: 0 0 20px #ff0066; }
}

.card {
    background: rgba(255,255,255,0.8);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    text-align: center;
    font-size: 20px;
}

.stButton>button {
    background-color: #f4b400;
    color: white;
    border-radius: 25px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="big-title">🌷 Thank You Nisha Mam 🌷</p>', unsafe_allow_html=True)

st.write("")

# Button to Show Message
if st.button("Click to Open Special Message 💌"):
    st.markdown("""
    <div class="card">
    <h2>Dear Nisha Mam ❤️</h2>
    <p>
    Tusi sade layi sirf teacher nahi,<br>
    tusi ik inspiration ho.<br><br>
    Tuhade bina class hamesha adhuri lagegi,<br>
    par tuhadi sikhlayi zindagi bhar saath rahegi.<br><br>
    Thank you for everything 🌸
    </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("✨ We Will Always Be Grateful ✨")
