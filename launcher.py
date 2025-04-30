import streamlit as st
import subprocess
import sys
import os

st.set_page_config(page_title="ProLabs Launcher", layout="centered")

# === Custom CSS Styling ===
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #0f2027, #203a43, #2c5364);
            color: white;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }

        .title {
            font-size: 60px;
            font-weight: bold;
            background: -webkit-linear-gradient(left, #00f0ff, #ff00ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: 40px;
            margin-bottom: 60px;
            text-align: center;
        }

        .button-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 25px;
        }

        .stButton > button {
            font-size: 18px;
            font-weight: bold;
            width: 200px; /* Button width */
            height: 60px; /* Button height */
            border-radius: 30px; /* Rounded corners */
            border: none;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 0 8px rgba(0, 0, 0, 0.3);
            text-transform: uppercase;
        }

        /* Play Button Styling */
        .stButton.play-btn > button {
            background-color: #00c9a7;  /* Teal color */
            color: white;
        }

        .stButton.play-btn > button:hover {
            background-color: #00e6bf;  /* Lighter teal on hover */
            color: black;
            transform: scale(1.05);
            box-shadow: 0 0 15px #00fff0;
        }

        /* Exit Button Styling */
        .stButton.exit-btn > button {
            background-color: #e74c3c;  /* Red color */
            color: white;
        }

        .stButton.exit-btn > button:hover {
            background-color: #ff6f61;  /* Lighter red on hover */
            color: black;
            transform: scale(1.05);
            box-shadow: 0 0 15px #ff9999;
        }
    </style>
""", unsafe_allow_html=True)

# === Title ===
st.markdown('<div class="title">🔥 ProLabs 🔥</div>', unsafe_allow_html=True)

# === Centered Button Stack ===
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Play Button
with st.form("play_form"):
    st.markdown('<div class="stButton play-btn">', unsafe_allow_html=True)
    play = st.form_submit_button("▶ Play")
    st.markdown('</div>', unsafe_allow_html=True)
    if play:
        try:
            subprocess.Popen([sys.executable, os.path.abspath("main.py")])
            st.success("Game launched successfully!")
        except Exception as e:
            st.error(f"Failed to launch game: {e}")

# Exit Button
with st.form("exit_form"):
    st.markdown('<div class="stButton exit-btn">', unsafe_allow_html=True)
    exit_game = st.form_submit_button("✖ Exit")
    st.markdown('</div>', unsafe_allow_html=True)
    if exit_game:
        st.warning("Exit clicked. Please close the tab or stop the app.")

st.markdown('</div>', unsafe_allow_html=True)
