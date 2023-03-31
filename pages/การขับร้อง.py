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
path = f"./audio/ขับร้องเพลงไทยเดิม/"

with st.container():
    file = st.select_slider(
        'Select a color of the rainbow',
        options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'])
    # audio_file = open('../audio/ขับร้องเพลงไทยเดิม/'+ color +'.wav', 'rb')
    blobs = bucket.list_blobs(prefix=os.path.join(path,file))
    blobs_full = [file.name for file in blobs]
    blobs_cut = [file.replace(os.path.join(path,file)+'/', '') for file in blobs_full]
    for audio_list , audio_file in zip(blobs_cut, blobs_full):
        st.write(audio_list)
        blob = bucket.blob(audio_file)
        with blob.open("rb") as f:
            st.audio(f.read(), format="audio/wav")   
    # audio_bytes = audio_file.read()

    # st.audio(audio_bytes, format='audio/wav')