"""
Contact Page using formsubmit.co API
"""
import streamlit as st
from streamlit_lottie import st_lottie
from utils import *


st.set_page_config(
        page_title="AI Audio Transciber",
        page_icon="🎵",
        layout= "wide",
        initial_sidebar_state="expanded",
        menu_items={
        'Get Help': 'https://github.com/smaranjitghose/AIAudioTranscriber',
        'Report a bug': "https://github.com/smaranjitghose/AIAudioTranscriber/issues",
        'About': "## A minimalistic application to generate transcriptions for audio built using Python"
        } )



st.title(":mailbox: Get In Touch With Me!")
hide_footer()

# Load Stylesheet(s) for relevant components
css_local("assets/styles/contact.css")
# Load and display animation
anim = lottie_local("assets/animations/contact.json")
st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium", # low; medium ; high
            # renderer="svg", # canvas
            height=400,
            width=400,
            key=None,
            )
# HTML code for formsubmit contactform template
contact_form = """
            <form action="https://formsubmit.co/b2365a7af4d69269a92869bf9be52f1ba" method="POST">
            <input type="hidden" name="_captcha" value="true">
            <input type="hidden" name="_template" value="table">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here"></textarea>
            <button type="submit">Send</button>
            </form>
            """
st.markdown(contact_form,unsafe_allow_html=True)

