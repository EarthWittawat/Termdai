from PIL import Image
import streamlit as st
from audiorecorder import audiorecorder
from pathlib import Path
import pathlib
import os
import os.path

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
    st.header("ระบบเปิดรับชุดข้อมูลแบบทดสอบเพลงไทยเดิม 🎤")
    data_check = f"./audio/"
    count = {}
    for audio in os.listdir(data_check):
        st.subheader(audio)
        for audio_ex in os.listdir(os.path.join(data_check, audio)):
            for root_dir, cur_dir, files in os.walk(
                os.path.join(data_check, audio, audio_ex)
            ):
                count[audio_ex] = len(files)
                st.write(f'ต้องการเสียง "{audio_ex}" อีก {100 - len(files)} เสียง')
    st.write("")
    type = st.selectbox("หัวข้อแบบฝึกหัด", ["การเปล่งเสียงกลุ่มคำ", "กลวิธีขับร้อง"])
    if type == "การเปล่งเสียงกลุ่มคำ":
        list_1 = st.selectbox("เลือกเสียง", ["เออ", "อี"])
        audio = audiorecorder("Click to record", "กำลังบันทึกเสียง")
        if len(audio) > 0:
            # To play audio in frontend:
            st.audio(audio.tobytes())

            # To save audio to a file:
            count = 1
            path = f"./audio/{type}/{list_1}"
            isExist = os.path.exists(path)
            if not isExist:
                os.makedirs(path)
            for root_dir, cur_dir, files in os.walk(path):
                count += len(files)
            wav_file = open(f"./audio/{type}/{list_1}/{list_1}({count}).mp3", "wb")
            wav_file.write(audio.tobytes())
    if type == "กลวิธีขับร้อง":
        list_1 = st.selectbox("เลือกกลวิธีขับร้อง", ["การกลิ้งเสียง", "การเกลือกเสียง"])
        audio = audiorecorder("Click to record", "กำลังบันทึกเสียง")
        if len(audio) > 0:
            # To play audio in frontend:
            st.audio(audio.tobytes())

            # To save audio to a file:
            count = 1
            path = f"./audio/{type}/{list_1}"
            isExist = os.path.exists(path)
            if not isExist:
                os.makedirs(path)
            for root_dir, cur_dir, files in os.walk(path):
                count += len(files)
            wav_file = open(f"./audio/{type}/{list_1}/{list_1}({count}).mp3", "wb")
            wav_file.write(audio.tobytes())
