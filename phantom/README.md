# 🕯️ Welcome to the Phantom Chronicles 🕯️  
*An Escape Mystery Experience powered by MONGODB ATLAS*

---

🕸️ The **heavy iron gates** of **Blackstone Penitentiary** creak open before you, their rusted hinges *screaming like the tormented souls* trapped within.  

A cold wind howls through the darkness, carrying the scent of **damp stone** and **despair** 🥶 as you step into the shadow of its towering granite walls. 🧱

---

## 🕯️💀 The Curse Awakens 💀🕯️

Since the cursed New Year's Eve, **whispers** have haunted the halls of Cell Block 2...  

Home to the infamous 👻 **"Phantom of Blackstone"**

What began as flickering lights and icy drafts has now escalated into **full-blown terror**... 😱

---

## 📜 The Warden’s Briefing

> 🔐 *"Listen carefully, investigator..."*

- 🩸 **Six inmates** are dead this month — their faces frozen in **soul-wrenching terror**
- 🧠 Others claim they’re **whispered to in the dead of night**.....a voice like **grinding stone** that drills into their skulls
- They call it: **“The Phantom’s Whisper”** 🗣️👁️‍🗨️

> 📰 The state wants this contained before the **media circus** begins 🎥

---

## 🚨 YOUR MISSION 🚨

🕵️‍♂️ **Investigate** the strange happenings  
🧩 **Solve** each clue to get closer to the truth  
🗡️ **Uncover** what’s really happening behind these haunted walls...

- ❓ Who is behind the inmate deaths?  
- ⚰️ How are the inmates dying?  
- 🎭 Can you prove it’s just an *elaborate hoax*... or is it something more?

---

⚠️ **Let the horror begin... 🔦🗝️🕳️**

---

## Pre-requisites
- Python3 >= 3.12
- MongoDB Compass installed
  
## Getting Started for Admin
- Load phantom datasets from this [folder](https://drive.google.com/drive/folders/14ayQBGqtL7VM6Eg5fejNtuYuySf5NjEP) to any database of your choice
- Share credentials for running aggregation pipelines via Compass

## Getting Started for Participants
- Clone repository
```
git clone https://github.com/vinodkrishnan23/Escape-Games.git
git checkout phantom
git pull origin phantom
```
- Install all python libraries - strealit,pymongo etc.
```
cd Escape-Games
python3 -m pip install -r requirement.txt
```
- Ask Admin for your mongodb atlas connection string and dbname with pre-loaded data
- Modify .secrets.toml file within .streamlit folder with above details
```
MONGODB_URI = "YOUR MONGODB ATLAS Connection String"
DB_NAME = "YOUR DB NAME"
```
- Run the application
```
streamlit run registrations.py
```
- Register with your name and email
- MongoDB Team will share credentials to access Atlas Cluster via Compass
- Start the quiz


