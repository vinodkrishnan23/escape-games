import streamlit as st
from session_utils import load_question, update_user_in_db
from datetime import datetime
import json
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Escape Game", layout="centered")
st.markdown("""
    <style>
    /* Make all text in the sidebar uppercase */
    section[data-testid="stSidebar"] * {
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Styling remains untouched
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

from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    prefix="escape_game_",
    password="12345"
)

if not cookies.ready():
    st.stop()

# ⛔️ Load session user
if not st.session_state.get("user"):
    user_info = json.loads(cookies["user"])
    if user_info:
        st.session_state.user = {
            "email": user_info["email"],
            "name": user_info["name"]
        }
        st.session_state.current_question = int(cookies["current_question"])
        st.session_state.score = int(cookies["score"])
    else:
        st.warning("Please register to play.")
        st.switch_page("registrations.py")
        st.stop()

# 🧠 Init session vars
if "score" not in st.session_state:
    st.session_state.score = 0
if "show_next" not in st.session_state:
    st.session_state.show_next = False
if "show_submit" not in st.session_state:
    st.session_state.show_submit = True
if "last_score_message" not in st.session_state:
    st.session_state.last_score_message = ""

# ✅ Load current question
q = load_question(st.session_state.current_question)

# 🏁 End screen
if not q:
    st.success("🎉 You've completed all puzzles!")
    st.write(f"Your final score: {st.session_state.score}")
    if st.button("🏆 View Leaderboard"):
        st.switch_page("pages/leaderboard.py")
    st.stop()

# ⏱ Start time
if "start_time" not in st.session_state or st.session_state.start_time is None:
    st.session_state.start_time = datetime.utcnow()

# 🧩 Question UI
st.title(f"🧩 Question #{q['sort_order']}")
st.subheader(q["question"])
with st.expander("Hint 🔍"):
    st.write(q["hint"])

user_answer = st.text_area("Your Answer:")

# 👀 Show last score message until user moves to next question
if st.session_state.last_score_message:
    st.success(st.session_state.last_score_message)

# 🎯 Conditional Button: Show either Submit or Next in same position
if st.session_state.show_submit:
    if st.button("Submit Answer"):
        def normalize(txt): return txt.strip().lower()

        if normalize(user_answer) == normalize(q["answer"]):
            time_taken = (datetime.utcnow() - st.session_state.start_time).total_seconds()
            bonus = max(0, 100 - int(time_taken / 5))
            earned = 500 + bonus
            st.session_state.score += earned

            update_user_in_db(st.session_state.score, st.session_state.current_question)
            cookies["score"] = str(st.session_state.score)
            cookies.save()

            # Save the score message in session state
            st.session_state.last_score_message = f"✅ Correct! You earned {earned} points. Total score: {st.session_state.score}"

            st.session_state.show_submit = False
            st.session_state.show_next = True
            st.rerun()
        else:
            st.error("❌ Try again!")

elif st.session_state.show_next:
    if st.button("Next Question"):
        st.session_state.current_question += 1
        cookies["current_question"] = str(st.session_state.current_question)
        cookies.save()

        st.session_state.show_next = False
        st.session_state.show_submit = True
        st.session_state.start_time = None
        st.session_state.last_score_message = ""  # ✅ Clear after moving to next
        st.rerun()