import streamlit as st

color = st.select_slider(
    'Select a color of the rainbow',
    options=['1', '2', '3', '4', '5', '6', '7'])
st.write('My favorite color is', color)