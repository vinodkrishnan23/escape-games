import streamlit as st
from mongodb import get_db
from datetime import datetime

def init_session():
    if "user" not in st.session_state:
        st.session_state.user = None
        st.session_state.score = 0
        st.session_state.current_question = 1
        st.session_state.start_time = None

def login_user(email):
    db = get_db()
    user = db["registrations"].find_one({"email": email})
    if user:
        st.session_state.user = user
        st.session_state.score = user.get("score", 0)
        st.session_state.current_puzzle = user.get("current_puzzle", 1)
        return True
    return False

def load_question(sort_order):
    db = get_db()
    return db["questions"].find_one({"sort_order": sort_order})

def update_user_in_db(score, current_question):
    db = get_db()
    now = datetime.utcnow()
    db["registrations"].update_one(
        {"email": st.session_state.user["email"]},
        {"$set": {
            "score": score,
            "current_question": current_question,
            "last_question_time": now
        }}
    )
    st.session_state.user["score"] = score
    #st.session_state.user["current_question"] = current_question