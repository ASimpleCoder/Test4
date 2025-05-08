import streamlit as st

pressed = st.button("Hello Guys Press Me")
while True:
  if pressed:
    st.write("You pressed the button")
    break
