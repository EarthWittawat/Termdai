from PIL import Image
import streamlit as st
from audiorecorder import audiorecorder
from pathlib import Path
import pathlib
import os
import os.path
import csv
import pandas as pd

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
    header = ['report', 'สถานะ']
    st.dataframe(pd.read_csv('report.csv'))
    report = st.text_input(
        "แจ้งปัญหา 👇",
    )
    if st.button('ยืนยัน'):
        st.success('ดำเนินการเสร็จสิ้น')
        with open('report.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)

            # write the data
            writer.writerow([report, 'กำลังตรวจสอบ'])
