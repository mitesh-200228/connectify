import streamlit as st
import behind_process

st.title('Connectify!')
user_input = st.text_input('Enter a linkedin profile:', 'Hello, User!')

if st.button('Submit'):
    data = behind_process.func(user_input)
    if(data == []):
        st.error("No data found for this profile.")
    else:
        dt = behind_process.model()
        st.write(dt)
        # st.write(data)
    # st.switch_page("pages/page_1.py")