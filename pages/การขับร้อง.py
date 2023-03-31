import streamlit as st

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['1', '2', '3', '4', '5', '6', '7'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)