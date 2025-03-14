import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
HEADERS = {"Authorization": "Bearer API KEY"}  

st.title("📖 AI Story Generator")
st.write("Enter a prompt to generate a well-structured story!")


title = st.text_input("Enter a story title:", "The Lost Kingdom")  
story_prompt = st.text_area("Describe your story idea:", "A brave knight embarks on a quest to find a lost treasure.")

def query_huggingface_api(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return response.json()

if st.button("Generate Story"):
    if story_prompt.strip():
        with st.spinner("Generating..."):
            payload = {"inputs": story_prompt, "parameters": {"max_length": 200, "temperature": 0.5}}
            
            result = query_huggingface_api(payload)
            generated_text = result[0]["generated_text"] if isinstance(result, list) else "Error: " + str(result)

            story = generated_text.replace(story_prompt, "").strip()

            st.write(f"## 📖 {title}") 
            st.write(story)
    else:
        st.warning("Please enter a story idea!")
