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
st.image('./header.png')
