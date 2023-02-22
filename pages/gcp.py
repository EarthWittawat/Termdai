import streamlit as st
from google.oauth2 import service_account
from google.cloud import storage

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = storage.Client(credentials=credentials)

# Retrieve file contents.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache 
def read_file(bucket_name, file_path):
    bucket = client.bucket(bucket_name)
    content = bucket.blob(file_path).download_as_string().decode("utf-8")
    return content

bucket_name = "termdai-bucket"
file_path = "report.csv"

content = read_file(bucket_name, file_path)

# Print results.
for line in content.strip().split("\n"):
    report, สถานะ = line.split(",")
    st.write(f"{report} has a :{สถานะ}:")