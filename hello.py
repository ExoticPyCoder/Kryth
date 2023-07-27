import streamlit as st
st.header("hello world")
st.text("apple")
st.text("banana")
st.text("orange")
st.button('Click here')
st.radio('Pick one', ['cats', 'dogs'])
st.color_picker('Pick a color')
st.multiselect('Buy', ['milk', 'apples', 'potatoes'])
st.slider('Pick a number', 0, 100)
with st.form(key='my_form'):
username = st.text_input('Username')
Password = st.text_input('Password')
st.form_submit_button('Login')
