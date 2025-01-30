import streamlit as st
import google.generativeai as genai

# Configure the API key for Google Generative AI
genai.configure(api_key="AIzaSyDQNBRZOU1Wz99w57yNJuuuMKB__rZXHbc")

# Create the generative model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title("📖 AI STORY GENERATOR 📖")

# Input field for the user to enter a prompt/keywords
user_input = st.text_input("Enter keywords or a prompt for your story:")


if st.button("create story"):
    # Generate the story using the generative model
    prompt = f"create a story for children under 15 using thse keywords {user_input} create title too"
    response = model.generate_content(prompt)
    
    
    # Display the generated story
    
    st.write(response.text)