
import streamlit as st
from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

st.title("🎬 Movie Recommender AI")
st.write("Ask me anything about movies!")

question = st.text_input("What kind of movie are you looking for?", 
                          placeholder="e.g. I want a movie like Inception")

if st.button("Recommend"):
    if question:
        with st.spinner("Finding the best movies for you..."):
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are a movie recommendation expert. Give 3 movie recommendations with brief reasons. Be specific and helpful."},
                    {"role": "user", "content": question}
                ]
            )
            st.success(response.choices[0].message.content)
    else:
        st.warning("Please enter a question first!")
