from PIL import Image
import streamlit as st
from audiorecorder import audiorecorder
from pathlib import Path
import pathlib
import os
import os.path
from google.oauth2 import service_account
from google.cloud import storage

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

bucket_name = "termdai-bucket"
file_path = "report.csv"
bucket = client.bucket(bucket_name)
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
    st.header("Termdai Data Collection 📁")
    st.header("ระบบเปิดรับชุดข้อมูลแบบทดสอบเพลงไทยเดิม 🎤")
    st.write("")
    st.subheader("ข้อพึงปฎิบัติ*")
    st.write("1.เมื่อบันทึกเสียงเสร็จสิ้นให้ผู้บันทึกทำการตรวจไฟล์เสียงที่บันทึกที่หน้า Dashboard ก่อนทำการบันทึกในครั้งถัดไป")
    st.write("2.หากตรวจพบเจอ Bug & Error สามารถแจ้งได้ที่หน้า Report")
    st.write("")
    data_check = f"./audio/"
    count = {}
    for audio in os.listdir(data_check):
        st.subheader(audio)
        for audio_ex in os.listdir(os.path.join(data_check, audio)):
            for root_dir, cur_dir, files in os.walk(
                os.path.join(data_check, audio, audio_ex)
            ):
                count[audio_ex] = len(files)
                st.write(
                    f'ต้องการเสียง "{audio_ex}" อีก {100 - len(files)} เสียง')
    st.write("")
    type = st.selectbox("หัวข้อแบบฝึกหัด", [
                        "การเปล่งเสียงกลุ่มคำ", "กลวิธีขับร้อง"])
    if type == "การเปล่งเสียงกลุ่มคำ":
        list_1 = st.selectbox("เลือกเสียง", ["เออ", "อี"])
        audio = audiorecorder("Click to record", "กำลังบันทึกเสียง")
        path = f"./audio/{type}/{list_1}"
        blobs = bucket.list_blobs(prefix=f"audio/{type}/{list_1}/")
        blobs_full = [file.name for file in blobs]
        st.write(len(blobs_full))
        if st.button('ยืนยัน'):
            if len(audio) > 0:
                # To play audio in frontend:
                st.audio(audio.tobytes())

                # To save audio to a file:
                count = 1
                isExist = os.path.exists(path)
                if not isExist:
                    os.makedirs(path)
                for root_dir, cur_dir, files in os.walk(path):
                    count += len(files)
                wav_file = open(
                    f"./audio/{type}/{list_1}/{list_1}({count}).mp3", "wb")
                wav_file.write(audio.tobytes())
  
                blob = bucket.blob(f"audio/{type}/{list_1}/{list_1}({count}).mp3")
                blob.upload_from_filename(f"./audio/{type}/{list_1}/{list_1}({count}).mp3")
    if type == "กลวิธีขับร้อง":
        list_2 = st.selectbox("เลือกกลวิธีขับร้อง", [
                              "การกลิ้งเสียง", "การเกลือกเสียง"])
        audio = audiorecorder("Click to record", "กำลังบันทึกเสียง")
        path = f"./audio/{type}/{list_2}"
        if st.button('ยืนยัน'):
            if len(audio) > 0:
            # To play audio in frontend:
                st.audio(audio.tobytes())
                # To save audio to a file:
                count = 1

                isExist = os.path.exists(path)
                if not isExist:
                    os.makedirs(path)
                for root_dir, cur_dir, files in os.walk(path):
                    count += len(files)
                wav_file = open(
                    f"./audio/{type}/{list_1}/{list_1}({count}).mp3", "wb")
                wav_file.write(audio.tobytes())
