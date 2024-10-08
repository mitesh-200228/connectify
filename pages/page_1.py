import streamlit as st
import behind_process

st.title('Connectify 2!')
# user_input = st.text_input('Enter a linkedin profile:', 'Hello, User!')

if st.button('Submit'):
    data = behind_process.model()
    print(data)
    st.write(data)