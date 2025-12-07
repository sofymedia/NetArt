import streamlit as st

st.set_page_config(page_title="Counseling", page_icon="🐆", layout="centered",
                   initial_sidebar_state="collapsed")

st.write(f"Your current trait is {st.session_state.goal1}")

st.image("Page4.png")
st.write(f"\"Good choice!"
         f" Well, there's more than one class to your schedule."
         f" What else makes your heart soar?\"")

# User dialogue options
firstchat = st.radio(
    " ",
    ["Discovering natural wonders",
     "Discovering new things about myself I never knew I was capable of",
     "This is corny af"],
     index=None
)

# Make a variable to hold the second trait
if "goal2" not in st.session_state:
    st.session_state.goal2 = "unknown"

# Assign the trait2 based on user's response
if firstchat == "Discovering natural wonders":
    st.session_state.goal2 = "Science"
elif firstchat == "Discovering new things about myself I never knew I was capable of":
    st.session_state.goal2 = "Self-Awareness"

# Next button functionality
if st.button("Next ➡"):
    if firstchat == "This is corny af":
        st.switch_page("pages/Offend.py")
    else:
        st.switch_page("pages/page5.py")