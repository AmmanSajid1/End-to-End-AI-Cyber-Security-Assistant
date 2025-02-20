import streamlit as st
import requests
import os

from dotenv import load_dotenv

load_dotenv()

# FastAPI endpoint (update if needed)
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/search/")

st.set_page_config(page_title="MITRE Chatbot", layout="wide")

# Chatbot UI
st.title("🔍 MITRE ATT&CK Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_query = st.chat_input("Ask me about MITRE ATT&CK...")

if user_query:
    # Display user query
    st.session_state["messages"].append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Send query to FastAPI backend
    response = requests.post(API_URL, json={"query": user_query})
    bot_reply = response.json().get("results", "Error: No response")

    # Display bot response
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
