import streamlit as st
from mongodb import get_db
import pandas as pd


st.set_page_config(page_title="Leaderboard", layout="wide")
st.title("☠️ PHANTOM's Leaderboard ☠️")
st.markdown("""
    <style>
    /* Make all text in the sidebar uppercase */
    section[data-testid="stSidebar"] * {
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# 🕒 Auto-refresh every 20 seconds
refresh_interval = 1
st.markdown(
    f"<script>setTimeout(function() {{ window.location.reload(); }}, {refresh_interval * 1000});</script>",
    unsafe_allow_html=True,
)

db = get_db()
players = list(db["registrations"].find({"score":{"$exists":1}}, {"_id": 0, "name": 1, "email": 1, "score": 1}))

if not players:
    st.info("No players registered yet.")
    st.stop()

# Sort by score descending
players.sort(key=lambda x: int(x["score"]), reverse=True)

# Add ranks
for i, player in enumerate(players):
    player["rank"] = i + 1

# Convert to DataFrame
df = pd.DataFrame(players)

# 🔍 Search by name/email
search_query = st.text_input("🔍 Search for a player by name or email").strip().lower()
if search_query:
    df = df[df["name"].str.lower().str.contains(search_query) | df["email"].str.lower().str.contains(search_query)]

# 🌟 Highlight top 3 with emojis
def highlight_row(row):
    if row["rank"] == 1:
        return ["🥇 " + str(row["rank"]), row["name"], row["email"], row["score"]]
    elif row["rank"] == 2:
        return ["🥈 " + str(row["rank"]), row["name"], row["email"], row["score"]]
    elif row["rank"] == 3:
        return ["🥉 " + str(row["rank"]), row["name"], row["email"], row["score"]]
    else:
        return [str(row["rank"]), row["name"], row["email"], row["score"]]

# Apply row highlights
highlighted_data = df.apply(highlight_row, axis=1, result_type="expand")
highlighted_data.columns = ["Rank", "Name", "Email", "Score"]

# Display table
st.dataframe(highlighted_data, use_container_width=True, hide_index=True)
