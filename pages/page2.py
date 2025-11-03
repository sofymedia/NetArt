import streamlit as st

#Checking that the session state variable works
#st.write(st.session_state.name)

st.image("RoaryThinkWIP.png")
st.write(f"\"Nice to see you {st.session_state.name}!"
         f" What types of classes are you interested in registering for?\"")

firstchat = st.radio(
    " ",
    ["This previous semester was so boring! Give me something interesting!",
     "NONE! I think you're STINKY!"],
    captions=[
        "",
        "",
    ], index=None
)

if st.button("Next ➡"):
    if firstchat == "This previous semester was so boring! Give me something interesting!":
        st.switch_page("pages/page3.py")
    if firstchat == "NONE! I think you're STINKY!":
        st.switch_page("pages/Offend.py")

