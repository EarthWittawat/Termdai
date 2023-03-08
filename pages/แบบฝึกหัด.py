from PIL import Image
import streamlit as st
from audiorecorder import audiorecorder
from pathlib import Path
import pathlib
import os
import os.path
from google.oauth2 import service_account
from google.cloud import storage
from fastbook import *
import torch

st.set_page_config(
    page_title="Termdai",
    layout="wide",
)
with st.sidebar:
    st.header("About this Project✔")
    st.header("Developers👨‍💻")
    st.text("Wittawat Kitipatthavorn\nSoraat Treenuson\nPatcharapol Klinon")
    st.text(
        "ติดต่อ\nFacebook: Wittawat Kitipatthavorn\nTel: 086-398-1093\nLine: wittawat_earth"
    )
with st.container():
    audio = audiorecorder("Click to record", "กำลังบันทึกเสียง")