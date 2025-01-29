import streamlit as st
from models.gemini import GeminiAssist


st.title("Quick Edit Resume")
st.write(
    "Let's give the best for every opportunity"
)

with st.sidebar:
    gemini_key = st.text_input("Gemini API Key", key="gemini_api_key", type="password")
    "[Get an Gemini API key](https://aistudio.google.com/app/apikey)"

    open_ai_key = st.text_input("OpenAI API Key",type="password")
    "[Get OpenAI API Key](https://platform.openai.com/api-keys)"