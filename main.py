import streamlit as st
import behind_process
import pandas as pd

st.title('Connectify!')
user_input = st.text_input('Enter a linkedin profile:', 'Hello, User!')

if st.button('Submit'):
    # data = []
    data = behind_process.func(user_input)
    print(data)
    if(data == []):
        st.error("No data found for this profile or user already exist, try different profile.")
    else:
        dt,person = behind_process.model()
        new_row = pd.Series(['Main Person','Most Matched Person','2nd Most Matched Person','3rd Most Matched Person'],index=dt.columns)
        dt.loc[-1] = new_row
        dt.sort_index(inplace=True)
        # dt.rename(columns={'0':'Main Person','1':'Most Matched Person','2':'2nd Most Matched Person','3':'3rd Most Matched Person'},inplace=True)
        st.write(dt)

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# def login():
#     if st.button("Log in"):
#         st.session_state.logged_in = True
#         st.rerun()

# def logout():
#     if st.button("Log out"):
#         st.session_state.logged_in = False
#         st.rerun()

# login_page = st.Page(login, title="Log in", icon=":material/login:")
# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
# rooms = st.Page("reports/rooms.py",title="Rooms", icon=":material/logout:")
# create_room = st.Page("reports/create_room.py",title="Create Room", icon=":material/create:")

# dashboard = st.Page("reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
# bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
# alerts = st.Page("reports/alerts.py", title="System alerts", icon=":material/notification_important:")

# # search = st.Page("tools/search.py", title="Search", icon=":material/search:")
# # history = st.Page("tools/history.py", title="History", icon=":material/history:")

# if st.session_state.logged_in:
#     pg = st.navigation(
#         {
#             "Account": [logout_page],
#             "Reports": [create_room, rooms],
#         }
#     )
# else:
#     pg = st.navigation([login_page])

# pg.run()