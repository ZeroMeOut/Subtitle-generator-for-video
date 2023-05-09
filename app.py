import streamlit as st
from dict import lang, translators
from utilities import *
import os

option1 = st.selectbox(
    'Video Language',
    lang.keys())
st.write("\n")

option2 = st.selectbox(
    'Preferred Language',
    lang.keys(), key=[index for index, value in enumerate(lang)])
st.write("\n")

option3 = st.selectbox(
    'Translator',
    translators.keys())
st.write("\n")

file = st.file_uploader("Upload a file", type=[".mov", ".mp4"])
st.write("\n")

if file is not None:
    with open(os.path.join("temp/video", file.name), "wb") as f:
        f.write(file.getbuffer())

col1, col2, col3 = st.columns(3)
with col2:
    if st.button('Generate Subtitles') and file is not None:
        PATH = "temp"
        video_audio(f"{PATH}/video/{file.name}", "original_audio")
        whisper_run()
        translator(option1, option2, option3)
        st.write("Your file is in temp/subtitles.")
