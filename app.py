import streamlit as st
from groq import Groq
import os

# ---------- Page Config ----------
st.set_page_config(
    page_title="CineMind AI",
    page_icon="🎬",
    layout="centered"
)

# ---------- Custom Futuristic CSS ----------
st.markdown("""
<style>
    body, .stApp {
        background: radial-gradient(circle at top, #0d1117 0%, #05060a 100%);
        color: #e6edf3;
    }
    .title-glow {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00f5d4, #7b2ff7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #9aa5b1;
        font-size: 1rem;
        margin-bottom: 30px;
    }
    .stTextInput input {
        background-color: #161b22 !important;
        color: #e6edf3 !important;
        border: 1px solid #30363d !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    .stButton button {
        background: linear-gradient(90deg, #00f5d4, #7b2ff7);
        color: black;
        font-weight: 700;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        transition: 0.3s;
        width: 100%;
    }
    .stButton button:hover {
        opacity: 0.85;
        transform: scale(1.02);
    }
    .result-card {
        background: #0f1420;
        border: 1px solid #30363d;
        border-left: 4px solid #00f5d4;
        border-radius: 12px;
        padding: 20px;
        margin-top: 25px;
        box-shadow: 0 0 20px rgba(0, 245, 212, 0.08);
        white-space: pre-wrap;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Groq Client ----------
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# ---------- UI ----------
st.markdown('<div class="title-glow">🎬 CineMind AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your personal AI movie curator — Hollywood, Bollywood & beyond</div>', unsafe_allow_html=True)

question = st.text_input(
    "",
    placeholder="e.g. I want a mind-bending movie like Inception"
)

if st.button("✨ Get Recommendations"):
    if question:
        with st.spinner("Scanning the multiverse of movies..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {"role": "system", "content": "You are a movie recommendation expert. Give 3 movie recommendations with brief reasons. Be specific and helpful. Format each as: **Movie Name** - reason."},
                        {"role": "user", "content": question}
                    ]
                )
                result = response.choices[0].message.content
                st.markdown(f'<div class="result-card">{result}</div>', unsafe_allow_html=True)
            except Exception:
                st.error("Something went wrong while getting recommendations. Please try again in a moment.")
    else:
        st.warning("Please enter a description first!")
