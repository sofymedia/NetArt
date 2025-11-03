import streamlit as st
import os

#Sets up site characteristics
st.set_page_config(page_title="Counseling", page_icon="🐆", layout="centered", 
                   initial_sidebar_state="collapsed")

#The homepage
st.title("✨ Welcome to a special college counseling appointment!")
st.write("*A Work-in-Progress Internet Art Project by Sofya Mashukova*")
#st.header("text")
#st.subheader("text")

st.divider()
#ChatGPT troubleshooting tips
st.write("Current working directory:", os.getcwd())
st.write("Files in current directory:", os.listdir())

#The first Roary image
st.image("RoaryWelcomeWIP.png")

st.write("\"Hello! What's your name?\"")

if "name" not in st.session_state:
    st.session_state.name = "Anonymous"

st.session_state.name = st.text_input("Enter name",label_visibility="hidden",placeholder="Enter...")
if st.button("Next ➡"):
    st.switch_page("pages/page2.py")





