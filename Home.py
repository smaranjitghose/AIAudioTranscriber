import streamlit as st
import streamlit_lottie

import pathlib
import requests
import whisper
from pytube import YouTube


from utils import lottie_local,css_local,hide_footer,st_lottie

def main():
    """
    Main Function
    """
    st.set_page_config(
        page_title="AI Audio Transciber",
        page_icon="▶️",
        layout= "centered",
        menu_items={
        'Get Help': 'https://github.com/smaranjitghose/AIAudioTranscriber',
        'Report a bug': "https://github.com/smaranjitghose/AIAudioTranscriber/issues",
        'About': "## A minimalistic application to generate transcriptions for audio built using Python"
        } )
    
    st.title("AI Audio Transcriber")
    hide_footer()
    # Load and display animation
    anim = lottie_local("assets/animations/transcriber.json")
    st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium", # low; medium ; high
            # renderer="svg", # canvas
            height=400,
            width=400,
            key=None)


    # Initialize Session State Variables
    if "page_index" not in st.session_state:
        st.session_state["page_index"] = 0
        st.session_state["model_type"] = ""
        st.session_state["input_mode"] = ""
        st.session_state["file_path"] = ""
        st.session_state["transcript"] = ""
        st.session_state["lang"] = ""

        
    # Create a Input Form Component
    input_mode = st.sidebar.selectbox(
                                    label="Input Mode",
                                    options= ["Upload Audio File", "Youtube Video URL", "Online Audio URL"])
    st.session_state["input_mode"] = input_mode

    # Create a Form Component on the Sidebar for accepting input data and parameters
    with st.sidebar.form(key="input_form",clear_on_submit=False):

        # Nested Component to take user input for audio file as per seleted mode
        if input_mode=="Upload Audio File":
            uploaded_file = st.file_uploader(
                    label="Upload your audio📁",
                    type=["wav","mp3","m4a"],
                    accept_multiple_files=False,
                    )
        elif input_mode == "Youtube Video URL":
            yt_url = st.text_input(label="Paste URL for Youtube Video ▶️")
        else:
            aud_url = st.text_input(label="Enter URL for Audio File 🔗 ")
        
        # Nested Component for model size selection
        st.session_state["model_type"] = st.radio(label="Choose Model Size 📦",
                    options=["base","tiny","small","medium"])
        
        # Nested Optional Component to select segment of the clip to be used for transcription
        extra_configs = st.expander("Choose Segment ✂")
        with extra_configs:
            start = st.number_input("Start time for the media (sec)", min_value=0, step=1)
            duration = st.number_input("Duration (sec) - negative implies till the end", min_value=-1,max_value=30, step=1)
        submitted = st.form_submit_button(label="Generate Transcripts✨")
        if submitted:

            # Create an inputs sub-directory if it does not exist already
            APP_DIR = pathlib.Path(__file__).parent.absolute()
            INPUT_DIR = APP_DIR / "input"
            INPUT_DIR.mkdir(exist_ok=True)


            # Load Audio File to Server as per input mode
            if input_mode=="Upload Audio File":
                if uploaded_file is not None:
                    grab_uploaded_file(uploaded_file, INPUT_DIR)
                    get_transcripts()
                else:
                    st.warning("Please🙏 upload a relevant audio file")
            elif input_mode == "Youtube Video URL":
                if yt_url and yt_url.startswith("https://"):
                    grab_youtube_video(yt_url, INPUT_DIR )
                    get_transcripts()
                else:
                    st.warning("Please🙏 enter a valid URL for Youtube video")
            else:
                if aud_url and aud_url.startswith("https://"):
                    grab_youtube_video(aud_url, INPUT_DIR )
                    get_transcripts()
                else:
                    st.warning("Please🙏 enter a valid URL for desired video")
            

    if st.session_state["transcript"] != "" and st.session_state["lang"] != "":
        col1,col2 = st.columns([4,4],gap="medium")
        
        # Display the generated Transcripts
        with col1:
            st.markdown("### Detected language🌐:")
            st.markdown(f"{st.session_state['lang']}")
            st.markdown("### Generated Transcripts📃: ")
            st.markdown(st.session_state["transcript"])
        
        # Display the original Audio
        with col2:
            if st.session_state["input_mode"] == "Youtube Video URL":
                st.markdown("### Youtube Video ▶️")
                st.video(yt_url)
            st.markdown("### Original Audio 🎵")
            with open(st.session_state["file_path"],"rb") as f:
                st.audio(f.read())
            # Download button
            st.download_button(
                            label="Download Transcripts📥",
                            data = st.session_state["transcript"],
                            file_name="transcripts.txt",
                            mime = "text/plain")




def grab_uploaded_file(uploaded_file,INPUT_DIR:pathlib.Path):
    """
    Method to store the uploaded audio file to server
    """
    try:
        print("--------------------------------------------")
        print("Attempting to load uploaded audio file ...")
        # Extract file format
        upload_name = uploaded_file.name
        upload_format = upload_name.split(".")[-1]
        # Create file name
        input_name = f"audio.{upload_format}"
        st.session_state["file_path"] = INPUT_DIR / input_name
        # Save the input audio file to server
        with open(st.session_state["file_path"], "wb") as f:
            f.write(uploaded_file.read())
        print("Succesfully loaded uploaded audio")
    except:
        st.error("😿 Failed to load uploaded audio file")

def grab_youtube_video(url:str,INPUT_DIR:pathlib.Path):
    """
    Method to fetch the audio codec of a Youtube video and save it to server
    """
    try:
        print("--------------------------------------------")
        print("Attempting to fetch audio from Youtube ...")
        video = YouTube(url).streams.get_by_itag(140).download(INPUT_DIR, filename="audio.mp3")
        print("Succesfully fetched audio from Youtube")
        st.session_state["file_path"] = INPUT_DIR / "audio.mp3"
    except:
        st.error("😿 Failed to fetch audio from YouTube")

def grab_online_video(url:str,INPUT_DIR:pathlib.Path):
    """
    Method to fetch an online audio file and save it to server
    """
    try:
        print("--------------------------------------------")
        print("Attempting to fetch remote audio file ...")
        # Fetch file
        r = requests.get(url, allow_redirects=True)
        # Extract file format
        file_name = url.split("/")[-1]
        file_format = url.split(".")[-1]
        # Create file name
        input_name = f"audio.{file_format}"
        st.session_state["file_path"] = INPUT_DIR / input_name
        # Save to server storage
        with open(st.session_state["file_path"], "wb") as f:
            f.write(r.content)
        print("Succesfully fetched remote audio")
    except:
        st.error("😿 Failed to fetch audio file")


def get_transcripts():
    """
    Method to generate transcripts for the desired audio file
    """
    try:
        # Load Whisper
        model = get_model(st.session_state["model_type"])
        print(st.session_state["file_path"])
        # load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(st.session_state["file_path"])
        # audio = whisper.pad_or_trim(audio)
        # Pass the audio file to the model and generate transcripts
        result = model.transcribe(audio)
        # Grab the text and update it in session state for the app
        st.session_state["transcript"] = result["text"]
        st.session_state["lang"] = result["language"]
        st.balloons()
    except:
        st.error("😿 Model Failed to genereate transcripts")


@st.cache
def get_model(model_type:str):
    """
    Method to load Whisper model to disk
    """
    try:
        print("------------------------------")
        print("Attempting to load Whisper ...")
        model = whisper.load_model(model_type)
        print("Succesfully loaded Whisper")
        return model
    except:
        print("Failed to load model")
        st.error("😿 Failed to load model")


def detect_language(audio,model):
    """
    Method to use Whisper model to determine language of input audio file
    """
    try:
        print("------------------------------")
        print("Attempting to detect language ...")
        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(model.device)
        # detect the spoken language
        _, probs = model.detect_language(mel)

    except:
        st.error("😿 Model Failed to detect language")

if __name__ == "__main__":
    main()
