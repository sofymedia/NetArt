import streamlit as st

# Placeholder text
# st.write("continuing on... placeholder")
# This is the page where user can start to select classes though

st.set_page_config(page_title="Counseling", page_icon="🐆", layout="centered",
                   initial_sidebar_state="collapsed")

st.image("RoaryThinkWIP.png")
st.write(f"\"Well alright {st.session_state.name}!"
         f" I'm sorry to hear your classes were so dry."
         f" What are you feeling like learning now?\"")

# User dialogue options
firstchat = st.radio(
    " ",
    ["The complex past of society intrigues me.",
     "I can't help but fall in love with the arts.",
     "I need to shape the world with a hands-on skill!",
     "I'm not feeling any of these things, I actually think you're kinda lame"],
     index=None
)

# Make a variable to hold the first trait
if "goal1" not in st.session_state:
    st.session_state.goal1 = "unknown"

# Assign the trait1 based on user's response
if firstchat == "The complex past of society intrigues me.":
    st.session_state.goal1 = "Historical"
elif firstchat == "I can't help but fall in love with the arts.":
    st.session_state.goal1 = "Art"
elif firstchat == "I need to shape the world with a hands-on skill!":
    st.session_state.goal1 = "Mechanical/Skill"

# Next button functionality
if st.button("Next ➡"):
    if firstchat == "I'm not feeling any of these things, I actually think you're kinda lame":
        st.switch_page("pages/Offend.py")
    else:
        st.switch_page("pages/page4.py")