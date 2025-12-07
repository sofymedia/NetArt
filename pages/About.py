import streamlit as st

#Sets up site characteristics
st.set_page_config(page_title="About", page_icon="🐆", layout="centered",
                   initial_sidebar_state="collapsed")

#The homepage
st.title("✨ About Website")
st.header("*An Internet Art Project by Sofi*")

st.write("Ever feel frustrated that you can't take an interesting college class because"
         " it doesn't fit your requirements? Me too! That's why I developed this site to"
         " explore the idea of how classes are chosen in education."
         "\n"
         "\n"
         "This is my final project for ART3647C Internet Art. Internet art can be thought of"
         " as a genre that deals with everything related to, well, the internet, often making the"
         " most of online formats. Internet art often deals with appropriation, which is ethically making"
         " use of materials that are not your own. For this site, I used course names and descriptions"
         " from the catalogs of Florida International University (FIU) and the School of Visual Arts (SVA)."
         "\n"
         "\n"
         "The main character you see is Roary, FIU's panther mascot! "
         "For questions, feedback, or concerns, you can email me at roaryfeedback@gmail.com")

if st.button("🏠 Homepage"):
    st.switch_page("NetArtRoary.py")