import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

def text_to_speech(text):
    tts = gTTS(text)
    fp = BytesIO()
    tts.write_to_fp(fp)
    return fp

st.title("Text to Speech")

# Text input
text_input = st.text_area("Enter text:", "Hello, World!")

# Convert text to speech
if st.button("Convert to Speech"):
    audio_data = text_to_speech(text_input)
    st.audio(audio_data.getvalue(), format='audio/mp3')

