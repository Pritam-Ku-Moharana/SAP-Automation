import streamlit as st

USERS = {
    "pritam": "12345",
    "admin": "29102005"
}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -------------------------------- LOGIN PAGE --------------------------------
def login():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if USERS.get(username) == password:
            st.session_state.logged_in = True
            st.session_state.user = username
            st.success("Login Successful ✅")
            st.rerun()
        else:
            st.error("Invalid username or password ❌")

# -------------------------------- MAIN PAGE --------------------------------
def main_page():
    st.title("Enter the details")

    reporting_period_frm = st.number_input("Reporting Period From", step=1, format="%d")

    st.write("You entered:", reporting_period_frm)

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# ------------------------------ APP FLOW -----------------------------------
if st.session_state.logged_in:
    st.write(f"Welcome **{st.session_state.user}**")
    main_page()
else:
    login()

# hide streamlit chrome
st.markdown("""
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)
