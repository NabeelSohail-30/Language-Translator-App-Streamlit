import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os
from playsound import playsound

# Create a Streamlit app
st.title("Language Translator App")

# Input text
input_text = st.text_area("Enter the text you want to translate:")

# Language selection
language_codes = {
    "Auto": "auto",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Korean": "ko",
}

from_lang = st.selectbox("Translate from:", list(
    language_codes.keys()))  # Use language names
to_lang = st.selectbox("Translate to:", list(
    language_codes.keys()))  # Use language names

# Get the language code from the selected language name
from_lang_code = language_codes[from_lang]
to_lang_code = language_codes[to_lang]

# Initialize translated_text outside of button scopes
translated_text = None


# Translation function
def translate_text(input_text, from_lang_code, to_lang_code):
    if not input_text:
        return ""

    translator = Translator()
    translated_text = translator.translate(
        input_text, src=from_lang_code, dest=to_lang_code)
    return translated_text.text


# Translate button
if st.button("Translate"):
    with st.spinner("Translating..."):
        translated_text = translate_text(
            input_text, from_lang_code, to_lang_code)
        st.success("Translation complete!")
        st.write(f"Translated Text ({to_lang}):")
        st.write(translated_text)
