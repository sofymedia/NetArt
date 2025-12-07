import streamlit as st

#Sets up site characteristics
st.set_page_config(page_title="Counseling", page_icon="🐆", layout="centered", 
                   initial_sidebar_state="collapsed")

# st.navigation([
    # st.Page("NetArtRoary.py",  title="Home", icon="🏠"),
    # st.Page("pages/About.py", title="About", icon="❓"),
    # st.Page("pages/Offend.py", title="[Offend]", icon="😡"),
    # st.Page("pages/page2.py", title="[Page 2]", icon="🐆"),
    # st.Page("pages/page3.py", title="[Page 3]", icon="🐆"),
    # st.Page("pages/page4.py", title="[Page 4]", icon="🐆"),
    # st.Page("pages/page5.py", title="[Page 5]", icon="🐆"),
    # st.Page("pages/page6.py", title="[Page 6]", icon="🐆"),
    # st.Page("pages/Result.py", title="[Result]", icon="📚")
# ], position="hidden")

#The homepage
st.title("✨ Welcome to a special college counseling appointment!")
st.write("*An Internet Art Project by Sofi*")
#st.header("text")
#st.subheader("text")

st.divider()
#The first Roary image
st.image("RoaryWelcomeWIP.png")
st.write("\"Hello! What should I call you?\"")
st.write("*(Names are not collected)*")

if "name" not in st.session_state:
    st.session_state.name = "Anonymous"

st.session_state.name = st.text_input("Enter name",label_visibility="hidden",placeholder="Nickname...")

# Old page navigation button
if st.button("Next ➡"):
    st.switch_page("pages/page2.py")

# New page nav. button
# st.page_link("pages/page2.py", label="Next ➡")

if st.button("❓ About Website"):
    st.switch_page("pages/About.py")



