import streamlit as st
import requests 

API_KEY = "LlSLTg6ulObWDvr39790T15tuqMbaoeE"
API_URL = "https://api.mistral.ai/v1/chat/completions"

st.title("My AI Chatbot")
st.write("Write Your Prompt For Getting Answer")

user_input_box = st.text_input("Add Your Prompt")
if st.button("Done"):
    if user_input_box:
        api_setup={
            "Authorization": f"Bearer {API_KEY}", 
            "Content_Type": "application/json"
        }
        
        data = {
            "model": "mistral-small",
            "messages": [
                {
                    "role": "system", "content": "My Chatbot"}, {
                        "role": "user", "content": user_input_box
                    }
            ]
        }
        
        requests = requests.post(API_URL, headers=api_setup,json = data)
        if requests.status_code == 200:
            result= requests.json()
            answer= result.get("choices",[{}])[0].get("message", {}).get("content", "chatbot")
            st.write (f"My Chatbot{answer}")
        else:
            st.write("Chatbot")