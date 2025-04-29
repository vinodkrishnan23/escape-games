import streamlit as st
import json

# Set up page
st.set_page_config(page_title="PHANTOM'S VENGEANCE - A HighLevel Mystery", layout="wide")

st.markdown("""
    <style>
    /* Make all text in the sidebar uppercase */
    section[data-testid="stSidebar"] * {
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# Display escape room premise
st.markdown(
    """
    <style>
        .big-text {
            font-size: 24px;
            line-height: 1.8;
            padding: 2rem;
            text-align: justify;
        }
    </style>
    """,
    unsafe_allow_html=True
)
from streamlit_cookies_manager import EncryptedCookieManager

# Initialize cookie manager
cookies = EncryptedCookieManager(
    prefix="escape_game_",  # helps avoid name collisions
    password="12345"  # should be strong and secret in production
)

# Redirect if not registered
if not cookies.ready():
    st.stop()

if not st.session_state.get("user"):
    user_info = json.loads(cookies["user"])
    print(user_info)
    if user_info:
        st.session_state.user = {
            "email": user_info['email'],
            "name": user_info['name']
        }
    else:
        st.warning("Please register to play.")
        st.switch_page("registrations.py")
        st.stop()

st.title("🪦 PHANTOM'S VENGEANCE - A HighLevel Mystery! 🪦")

st.markdown('<div class="big-text">', unsafe_allow_html=True)
st.write("""
The heavy iron gates of Blackstone Penitentiary creak open before you, their rusted hinges screaming like the tormented souls within. A cold wind carrying the scent of damp stone and despair washes over you as you step into the shadow of the massive granite walls.""")

st.write("""Ever since this new years, whispers have circulated about prison cell 2 series- home to the infamous"Phantom of Blackstone.""")
st.write("""What began as occasional cold spots and flickering lights has escalated into something far more sinister.""")

st.write("""The Warden's Briefing: "Listen carefully, investigator.""")

st.markdown("""
- Six inmates have died this month - their faces frozen in terror
- The others report being rambled to in the dead of night....a voice like grinding stone that drills into their skulls.
- They're calling it 'The Phantom's Whisper.' 
""")

st.write("""The state wants this contained before the media circus begins.""")

st.write("""ATTENTION HIGHLEVEL INVESTIGATOR - YOUR MISSION - """)

st.markdown("""
- Who is behind the inmates deaths?
- How are the inmates dying?
- Prove it's all elaborate hoax
""")

if st.button(f"Ready PlayerOne - {st.session_state.user['name']}?"):
    st.switch_page("pages/questions.py")
    

st.markdown('</div>', unsafe_allow_html=True)
