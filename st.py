import streamlit as st
from annotated_text import annotated_text

# hardcoded demo users
USERS = {
    "pritam": "12345",
    "admin": "admin123"
}

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


# if logged in → show next page
if "logged_in" in st.session_state and st.session_state["logged_in"]:
    st.write(f"Welcome {st.session_state['user']}")
    st.write("Now you can see the dashboard here...")

# REMOVE STREAMLIT STYLE (menu, footer, header)
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)




