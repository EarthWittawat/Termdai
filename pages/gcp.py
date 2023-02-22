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
def list_cs_files(bucket_name): 
    storage_client = storage.Client()

    file_list = storage_client.list_blobs(bucket_name)
    file_list = [file.name for file in file_list]

    return file_list
test = list_cs_files(bucket_name)
st.write(test)