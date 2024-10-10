# import streamlit as st
# from streamlit_gsheets import GSheetsConnection

# st.title('Rooms!')
# user_input = st.text_input('Enter a room name:')

# # Create a connection object.
# conn = st.connection("gsheets", type=GSheetsConnection)

# df = conn.read(spreadsheet="https://docs.google.com/spreadsheets/d/1Ojzc65O7XcVWXPAAKcskGuB5a9oMhM8my10JbHWGHCQ/edit?usp=sharing")

# if st.button('Submit'):
#     # conn.create(spreadsheet="https://docs.google.com/spreadsheets/d/1Ojzc65O7XcVWXPAAKcskGuB5a9oMhM8my10JbHWGHCQ/edit?usp=sharing",worksheet="Rooms_List",data=user_input)
#     for row in df.itertuples():
#         st.write(f"{row.name} has a :")