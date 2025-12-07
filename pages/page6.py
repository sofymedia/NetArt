import streamlit as st

st.set_page_config(page_title="Counseling", page_icon="🐆", layout="centered",
                   initial_sidebar_state="collapsed")

st.write(f"Your current traits are {st.session_state.goal1}, {st.session_state.goal2}, and "
         f"{st.session_state.mood1}")

st.image("Page6.png")
st.write(f"\"Bear with me {st.session_state.name}, just one more question!"
         f"\n  "
         f"\n  "
         f" ... How are you feeling, really?\"")

# User dialogue options
firstchat = st.radio(
    " ",
    ["... I'm kind of a pessimist, to be honest. 🤔",
     "ADVENTUROUS!",
     "No, come on, just give me a wild card!",
     "This is taking too damn long"],
     index=None
)

# Make a variable to hold the fourth trait
if "mood2" not in st.session_state:
    st.session_state.mood2 = "unknown"

# Assign the trait4 based on user's response
if firstchat == "... I'm kind of a pessimist, to be honest. 🤔":
    st.session_state.mood2 = "Pessimist"
elif firstchat == "ADVENTUROUS!":
    st.session_state.mood2 = "Adventurous"
elif firstchat == "No, come on, just give me a wild card!":
    st.session_state.mood2 = "Random"

# Next button functionality
if st.button("Next ➡"):
    if firstchat == "This is taking too damn long":
        st.switch_page("pages/Offend.py")
    else:
        st.switch_page("pages/Result.py")