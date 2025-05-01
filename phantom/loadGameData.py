import os
import json
from pymongo import MongoClient
import streamlit as st
from bson import ObjectId

# MongoDB connection settings
MONGODB_URI = st.secrets["MONGODB_URI"].replace("mongodb+srv://", f"mongodb+srv://{st.secrets['DB_USER']}:{st.secrets['DB_USER']}@")  # Change if needed
DATABASE_NAME = st.secrets["DB_NAME"]        # Change your database name
DATA_DIRECTORY = "./data"  # Change this to your JSON files folder
fixed_docs = []

def load_json_files_to_mongodb():
    # Connect to MongoDB
    client = MongoClient(MONGODB_URI)
    db = client[DATABASE_NAME]

    # Iterate over all JSON files in the directory
    for filename in os.listdir(DATA_DIRECTORY):
        if filename.endswith(".json"):
            filepath = os.path.join(DATA_DIRECTORY, filename)
            collection_name = os.path.splitext(filename)[0]  # remove .json extension
            
            print(f"Loading {filename} into collection {collection_name}...")

            with open(filepath, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    fixed_docs = []
                    for doc in data:
                        if isinstance(doc.get("_id"), dict) and "$oid" in doc["_id"]:
                            doc["_id"] = ObjectId(doc["_id"]["$oid"])
                            fixed_docs.append(doc)
                    
                    # Insert the data
                    if isinstance(data, list):
                        db[collection_name].delete_many({})  # Clear existing data
                        db[collection_name].insert_many(fixed_docs)
                    elif isinstance(data, dict):
                        #db[collection_name].delete_many({})  # Clear existing data
                        db[collection_name].insert_one(fixed_docs)
                    else:
                        print(f"Unsupported JSON format in file: {filename}")
                    
                except json.JSONDecodeError as e:
                    print(f"Failed to parse {filename}: {e}")

    print("✅ All JSON files have been loaded into MongoDB.")

if __name__ == "__main__":
    load_json_files_to_mongodb()