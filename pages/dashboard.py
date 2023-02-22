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
    st.header("รายการชุดข้อมูลแบบฝึกเพลงไทยเดิม")
    type = st.selectbox("หัวข้อแบบฝึกหัด", ["การเปล่งเสียงกลุ่มคำ", "กลวิธีขับร้อง"])
    path = "audio/" + type
    ex1_list = ['เออ','อี']
    ex2_list = ['การกลิ้งเสียง', 'การเกลือกเสียง']
    # if os.path.exists(path):
    if type == "การเปล่งเสียงกลุ่มคำ":
        for audio in ex1_list:
            st.write(audio)
            blobs = bucket.list_blobs(prefix=os.path.join(path,audio))
            blobs = [file.name for file in blobs]
            st.write(blobs)
    if type == "กลวิธีขับร้อง":
        for audio in ex2_list:
            st.write(audio)
            blobs = bucket.list_blobs(prefix=os.path.join(path,audio))
            blobs = [file.name for file in blobs]
            blobs.replace('os.path.join(path,audio)', '')
            st.write(blobs)        
    #         for ex in blobs:
    #             st.write(ex)
    #             audio_file = open(f"{path}/{audio}/{ex}", "rb")
    #             audio_bytes = audio_file.read()

    #             st.audio(audio_bytes, format="audio/mp3")
    # else:
    #     st.write("no data")
