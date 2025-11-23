import streamlit as st

st.set_page_config(page_title="Counseling", page_icon="🐆", layout="centered",
                   initial_sidebar_state="collapsed")

st.write(f"Your current traits are {st.session_state.goal1} and {st.session_state.goal2}")

st.image("RoaryThinkWIP.png")
st.write(f"\"Hmm... I have ideas for two of your four classes, let's brainstorm the next ones!"
         f" What inspires you lately?\"")

# User dialogue options
firstchat = st.radio(
    " ",
    ["Any kind of knowledge makes me curious, the more niche the better.",
     "Poetry... song... music... anything so full of joy!",
     "Exploring nature... love seeing little plants and critters",
     "I wish I didn't have to click through this just to write a peer response"],
     index=None
)

# Make a variable to hold the third trait
if "mood1" not in st.session_state:
    st.session_state.mood1 = "unknown"

# Assign the trait3 based on user's response
if firstchat == "Any kind of knowledge makes me curious, the more niche the better.":
    st.session_state.mood1 = "Curious"
elif firstchat == "Poetry... song... music... anything so full of joy!":
    st.session_state.mood1 = "Romantic/Joyous"
elif firstchat == "Exploring nature... love seeing little plants and critters":
    st.session_state.mood1 = "Nature"

# Next button functionality
if st.button("Next ➡"):
    if firstchat == "I wish I didn't have to click through this just to write a peer response":
        st.switch_page("pages/Offend.py")
    else:
        st.switch_page("pages/page6.py")