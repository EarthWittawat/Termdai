import streamlit as st

color = st.select_slider(
    'Select a color of the rainbow',
    options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'])
st.write('My favorite color is', color)