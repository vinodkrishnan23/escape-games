from session_utils import init_session
init_session()
import json
import streamlit as st
from mongodb import get_db

# 👇 Hide the sidebar completely

st.set_page_config(page_title="Register", layout="centered")
st.markdown("""
    <style>
    input, textarea {
        border: 2px solid #0B6623 !important;
        border-radius: 8px !important;
    }
    input:focus, textarea:focus {
        outline: none !important;
        border-color: #0B6623 !important;
        box-shadow: 0 0 5px #0B6623;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* Make all text in the sidebar uppercase */
    section[data-testid="stSidebar"] * {
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

from streamlit_cookies_manager import EncryptedCookieManager
# Initialize cookie manager
cookies = EncryptedCookieManager(
    prefix="escape_game_",  # helps avoid name collisions
    password="12345"  # should be strong and secret in production
)

db = get_db()
collection = db["registrations"]

#st.title("🔐 PHANTOM'S VENGEANCE")
st.title("👣👣 PHANTOM'S VENGEANCE - A HighLevel Mystery")

with st.form("registration_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    submit = st.form_submit_button("Register")

    if submit:
        if name and email:
            collection.insert_one({"name": name, "email": email})
            st.success("You're registered!")

            # Set session state flag
            st.session_state.registered = True
            st.session_state.user = {"name": name, "email": email}
            st.session_state.score = 0
            st.session_state.current_question = 1
            cookies["user"]= json.dumps(st.session_state.user)
            cookies["score"]=str(0)
            cookies["current_question"]= str(1)
            cookies.save()
            print(json.loads(cookies["user"]))
            print(cookies["score"])
            print(cookies["current_question"])

            # Navigate to next page
            st.switch_page("pages/premise.py")
        else:
            st.error("Please enter both name and email.")
