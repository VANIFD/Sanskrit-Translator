import streamlit as st
import json

# --- Load translations ---
with open("data/translations.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

# --- Page configuration ---
st.set_page_config(
    page_title="Sanskrit Translator",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        color: #1f2937;
    }
    .stButton>button {
        background-color: #4f46e5;
        color: white;
        font-size: 16px;
        height: 45px;
        width: 100%;
        border-radius: 8px;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
    }
    .stSelectbox>div>div>div>select {
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("🌐 Sanskrit to Multilingual Translator")
st.markdown(
    "Enter a Sanskrit word and get translations in 20+ languages. "
    "Perfect for linguists, developers, and language enthusiasts!"
)

st.divider()

# --- Layout with two columns ---
col1, col2 = st.columns([2, 1])

with col1:
    # Sanskrit input
    word = st.text_input("Enter Sanskrit Word:", placeholder="उदाहरण: राम")

with col2:
    # Language selection
    languages = list(next(iter(translations.values())).keys())
    language = st.selectbox("Select Target Language:", languages)

st.divider()

# --- Display translation ---
if word:
    word = word.strip()
    if word in translations:
        translated_word = translations[word].get(language, "Translation not found")
        st.success(f"**Translation in {language}:** {translated_word}")
    else:
        st.error("Word not found in dataset. Try another Sanskrit word.")

# --- Footer ---
st.markdown("""
    <style>
    /* App background with gradient and abstract effect */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        background-size: cover;
        background-attachment: fixed;
        color: #ffffff;
    }

    /* Main container */
    .main {
        font-family: 'Segoe UI', 'Helvetica', sans-serif;
        color: #ffffff;
    }

    /* Input and select box styling */
    .stTextInput>div>div>input, 
    .stSelectbox>div>div>div>select {
        border-radius: 12px;
        padding: 10px;
        font-size: 16px;
        border: 1px solid #ffffff55;
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }

    /* Button styling */
    .stButton>button {
        background-color: #1f8ef1;
        color: white;
        font-size: 16px;
        height: 45px;
        width: 100%;
        border-radius: 12px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #5390ff;
    }

    /* Footer hidden */
    footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)
