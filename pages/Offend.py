import streamlit as st

st.image("RoaryOffendWIP.png")
st.write(f"\"Why did you even come here {st.session_state.name}!?"
         f" Someone should reread the Student Code of Conduct!\"")

if st.button("❓ About Website"):
    st.switch_page("pages/About.py")