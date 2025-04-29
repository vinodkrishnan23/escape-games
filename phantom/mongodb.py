from pymongo import MongoClient
import streamlit as st

def get_db():
    client = MongoClient(st.secrets["MONGODB_URI"].replace("mongodb+srv://", f"mongodb+srv://{st.secrets['DB_USER']}:{st.secrets['DB_USER']}@"),tls=True,tlsAllowInvalidCertificates=True)  # Or your Atlas URI
    return client[st.secrets["DB_NAME"]]
