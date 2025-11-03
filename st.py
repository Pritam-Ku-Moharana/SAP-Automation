import streamlit as st

USERS = {
    "Pritam": "12345",
    "Admin": "29102005"
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

    reporting_year = st.number_input("Reporting Year", min_value=2025, max_value=2125, step=1, format="%d")
    st.write("Reporting Year:", reporting_year)
        
    reporting_period_frm = st.number_input("Reporting Period From", min_value=1, max_value=12, step=1, format="%d")
    st.write("Reporting Period From:", reporting_period_frm)

    reporting_period_to = st.number_input("Reporting Period To", min_value=1, max_value=12, step=1, format="%d")
    st.write("Reporting Period To:",reporting_period_to)

    comparison_year = st.number_input("Comparison Year", min_value=2025, max_value=2125, step=1, format="%d")
    st.write("Comparison Year",comparison_year)

    comaprison_period_from = st.number_input("Comparison Per. From", min_value=1, max_value=12, step=1, format="%d")
    st.write("Comparison Period From",comaprison_period_from)
    
    comparison_period_to = st.number_input("Comparison Period To", min_value=1, max_value=12, step=1, format="%d")
    st.write("Comparison Period To",comparison_period_to)

    missing = []

    if not reporting_year:
        missing.append("reporting_year")
    if not reporting_period_frm:
        missing.append("reporting_period_frm")
    if not reporting_period_to:
        missing.append("reporting_period_to")   
    if not comparison_year:
        missing.append("reporting_year")
    if not comaprison_period_from:
        missing.append("reporting_period_frm")
    if not comparison_period_to:
        missing.append("reporting_period_to")

    if missing:
        st.error(f"Please fill mandatory fields: {', '.join(missing)}")
    else:
        st.success("Form submitted successfully ✅")




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


