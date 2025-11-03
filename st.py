import streamlit as st
from annotated_text import annotated_text
import time

# hardcoded demo users
USERS = {
    "pritam": "12345",
    "admin": "29102005"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

##############################################################################################################################
def login():
    st.title("Login Page")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.success("Login Successful ✅")
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
        else:
            st.error("Invalid username or password ❌")
##############################################################################################################################
def main_page():
    st.title("Enter the details")

    reporting_period_frm = st.number_input("Reporting Period frm")



##############################################################################################################################
# if logged in → show next page
if "logged_in" in st.session_state and st.session_state["logged_in"]:
    st.write(f"Welcome {st.session_state['user']}")
    st.write("Now you can see the dashboard here...")

    time.sleep(4)
    main_page()
    if st.button("Logout"):
        st.session_state.logged_in = False
else:
    login()
 
# REMOVE STREAMLIT STYLE (menu, footer, header)
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)






