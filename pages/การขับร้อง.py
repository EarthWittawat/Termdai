from PIL import Image
import streamlit as st
from audiorecorder import audiorecorder
from pathlib import Path
import pathlib
import os
import os.path
from google.oauth2 import service_account
from google.cloud import storage
col1, col2 = st.columns(2)
# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

bucket_name = "termdai-bucket"
bucket = client.bucket(bucket_name)



with st.container():
    with col1:
        st.subheader('ฝึกขับร้องเพลงไทยเดิม')
        st.markdown("***")
    option = st.selectbox(
    'เลือกเพลงที่ต้องการฝึก',
    ('ต้นเพลงฉิ่ง 3 ชั้น', 'แขกวรเทศ'))
    st.header(option)
    file = st.select_slider(
        'เลือกท่อนที่ต้องการฝึกร้อง',
        options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'])
    
    # audio_file = open('../audio/ขับร้องเพลงไทยเดิม/'+ color +'.wav', 'rb')
    path = "audio/ขับร้องเพลงไทยเดิม/" + file + '.wav'
    blob = bucket.blob(path)
    with blob.open("rb") as f:
        st.audio(f.read(), format="audio/wav")   
    st.markdown("***")