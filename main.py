import streamlit as st
import behind_process

st.title('Connectify!')
user_input = st.text_input('Enter a linkedin profile:', 'Hello, User!')

if st.button('Submit'):
    data = behind_process.func(user_input)
    st.write(data)