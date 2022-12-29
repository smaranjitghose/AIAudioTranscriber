# AI Audio Transcriber

<p align = "center"><img src = "./assets/transcriber.gif" height = 300 alt = "Wallet Icon"></p>

A minimalistic application to generate transcriptions for audio built using Python

## 📝 Basic Application WorkFlow 

```mermaid
flowchart LR 
    U([Cliemt])
    
    I{Choose\n Input Mode}
    U -----> I
    
    I1[YouTube Video URL] 
    I2[Upload Video File]
    I3[Upload Audio File]
    I ---> I1 & I2 & I3

    YTC{"Check if\n Audio is available?"}
    YTA("Download video\n from YouTube")
    YTV("Download video\n from YouTube")
    
    I1 ---> YTC
    YTC --yes---> YTA
    YTC --no---> YTV

    VTA["Convert Video to Audio"]
    YTV ---> VTA
    I2 ---> VTA

    LA["Load Audio File"]
    YTA & VTA & I3---> LA
    
    M{"Choose\n Model Type"}
    U -----> M

    M1[(Ramanujan)]
    M2[(Bose)]
    M3[(Raman)]
    M4[(Kalam)]
    M ---> M1 & M2 & M3 & M4

    LM[Load Relevant Whisper Model]
    M1 & M2 & M3 & M4 --> LM

    GT("Generate Transcripts")
    LA & LM ---> GT

    O1(["Detected \n Language"])
    O2(["Complete \nSubtitle Text"])
    O3(["Subtitles \nwith Timestamps"])
    GT ---> O1 & O2 & O3

    OF(["Original\n Audio or Video"])
    D{{"Display to Client"}}
    I ---> OF
    O1 & O2 & OF ---> D

    DO{"Choose\n Output Option"}
    D1["SRT\n File"]
    D2["VTT\n File"]
    D3["Text\n File"]
    DP["Process Subtitle Object"]
    DN{{"Download Button"}}

    O3 ---> DP
    U ---> DO
    DO ---> D1 & D2 & D3 ---> DP ---> DN

    subgraph Result
        D
        DN
    end
```

## 👇 Product Snapshots

**v.0.0.1**
<p align = "center"><img src = "./assets/demo_snapshot_v1.png" height = 300 width = 450 alt = "AITranscriber Snapshot"></p>

**v.0.0.2** (Transcribing a Youtube Video Explaining Whisper)
<p align = "center"><img src = "./assets/demo_snapshot_v2_1.png" height = 300 width = 450 alt = "AITranscriber Snapshot v2"></p>

**v.0.0.2** (Transcribing an English Song - Thinkin About It)
<p align = "center"><img src = "./assets/demo_snapshot_v2_2.png" height = 300 width = 450 alt = "AITranscriber Snapshot v2"></p>

**v.0.0.3** (Transcribing a [clip](https://www.youtube.com/watch?v=A1UjHboEypk) from [Lex Fridman's podcast](https://lexfridman.com/podcast/))

<p align = "center"><img src = "./assets/demo_snapshot_v3.png" height = 300 width = 450 alt = "AITranscriber Snapshot v3"></p>

**v.0.0.4** (Transcribing another [clip](https://www.youtube.com/watch?v=zxqjlWNVGNM) from [Lex Fridman's podcast](https://lexfridman.com/podcast/))

<p align = "center"><img src = "./assets/demo_snapshot_v4.png" height = 300 width = 450 alt = "AITranscriber Snapshot v4"></p>


## ⚒️ Set-Up Instructions

<p align = "center"><img src = "./assets/setup.gif" height = 300 alt = "SetUp Icon"></p>

- Ensure you have the latest stable version of [Python](https://www.python.org/downloads/) in your system

- Open your terminal / command prompt. 

- Clone the repository 
    ```
    git clone https://github.com/smaranjitghose/AIAudioTranscriber.git
    ```
- Change the directory to the cloned project
    
    ```
    cd AIAudioTranscriber
    ```

- Install the dependencies

    ```
    pip install -r requirements.txt
    ```

- Install ffmpeg on your system

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

- Load the application

    ```
    streamlit run .\Home.py
    ```

- If the app does not load by itself in your default browser, open a browser of your choice and navigate to  `http://localhost:8501`

- To stop the application, press `CTRL + C` in your terminal


## 🏗️ Future Work 

- [x] Download and use audio from Youtube Video
- [x] Download and use online audio file
- [x] Use Session States and Caching for Better UX
- [x] Display the language detected propely (without using the shortcode)
- [x] Generate Dedicated SRT,VTT files for transcripts (in addition to txt)
- [x] Update Model options to honour the name of prominent Indian Scientists
- [x] Option to limit/increase input model file size
- [x] Functionality to check the validity URL provided for Youtube Video
- [x] Add Custom Favicon File
- [x] Add Scrollable Text Area for Generated Transcripts
- [ ] Resolve bug: Youtube video with multiple audios should download default audio. 
    - Example: This [clip](https://www.youtube.com/watch?v=93L6gDVRrUY) from Huberman Lab is in English yet the script fetches the spanish audio codec from Youtube  

- [ ] Option to burn transcripts to video (in-app)

```python
import os
output_video = "final.mp4"

os.system(f"ffmpeg -i {input_video} -vf subtitles={subtitle} {output_video}")
```

- [ ] Video Summarization from transcripts

- [ ] Speaker Diarization
- [ ] Word Level Timestamps for transcripts
- [ ] Generate and Save ASS transcript file
- [ ] Option to burn word level timestamp transcripts to video (in-app)
- [ ] Word Level Speaker Diarization
- [ ] Re-dockerize the application for Cloud Hosting
- [ ] Optimize for GPU usage and server storage




## ✏️ Note 

<p align = "center"><img src = "./assets/notes.gif" height = 300 alt = "Note Icon"></p>

- To view the generated transcript file(s) in VS Code IDE install [Subtitles Editor](https://marketplace.visualstudio.com/items?itemName=pepri.subtitles-editor) extension
- To extensively edit/manipulate the generated transcript file(s) use the open source tool [Subtitle Edit](https://www.nikse.dk/subtitleedit) 
- For Streamlit Sharing, mentioning versions of the modules in requirements throws error at times
- Large Modelv2 outperforms all other versions of Whisper in terms of performance especially in Multi-lingual Transcription. However, it takes a 10 times more V-RAM than the base model and has longer inference time
- To quickly record audio from system microphone use [this](https://github.com/smaranjitghose/miscellaneous/blob/master/handypython/data/audio/audio_recording.py) Python Script:
    - Pre-requisities:

        ```
        pip install pyaudio wave
        ```
- Whisper is unable to read audio file from disk if ``python-ffmpeg`` or ``ffmpeg`` python pacakges are installed. It only works when ``ffmpeg-python`` python package is installed and not the former too

    ```
    # Remove all ffmpeg related python packages
    pip uninstall python-ffmpeg ffmpeg ffmpeg-python
    # Install the appropriate pacakge for ffmpeg
    pip install ffmpeg-python

    ```
- [Pixabay](https://pixabay.com/) has a great collection of copyright free, no royalty songs that one can use for testing the application
- Poor Performance for Kanada or Telegu songs (often language recognition itself fails) for base model. Example: Kantara movie's [Varaha Roopam](https://www.youtube.com/watch?v=gH_RYRwVrVM) Song

<p align = "center"><img src = "./assets/demo_snapshot_v2_3.png" height = 300 width = 450 alt = "AITranscriber Snapshot v2"></p>



## 🥊Deployment Options 

<p align = "center"><img src = "./assets/hosting.gif" height = 300 alt = "Hosting Icon"></p>

- [Streamlit Cloud](https://streamlit.io/cloud)
- [HuggingFace Spaces](https://huggingface.co/docs/hub/spaces)

- [Fly](https://fly.io/)
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [Cyclic](https://app.cyclic.sh/#/)

- [Heroku](https://www.heroku.com/)
- [Digital Ocean](https://www.digitalocean.com/)

- Google App Engine
- Amazon EC2 Instance
- Azure App

(**Using Google Colab/Kaggle as temporary MVP server**)

- [pyngrok](https://pyngrok.readthedocs.io/en/latest/index.html)
    - Step 1: Install pyngrok in Google Colab

        ```
        ! pip install pyngrok
        ```
    
    - Step 2: Sign-up in [ngrok](https://ngrok.com/) and get Authentication Token

    - Step 3: Authenticate
        
        ```python
           from pyngrok import ngrok
           ngrok.set_auth_token("xxx")
        ```
    - Step 4: Load the Streamlit App at port 8051, create a tunnel for it and reveal the public URL for the tunnel

        ```python
           !nohup streamlit run app.py --server.port 8051 &
           url = ngrok.connect(8051).public_url
           print(url)
        ```
    
    - Step 5: Share URL with client
     


- [localtunnel](https://github.com/localtunnel/localtunnel)
    - Step 1: Install localtunnel

        ```
        npm install -g localtunnel
        ```
    - Step 2

        ```
        streamlit run Home.py & npx localtunnel --port 8501
        ```
    
    - Step 3: Share URL with client


(**Using local server as temporary MVP server**)

- NGINX + Cloudfare/ngrok


## 🙏 Acknowledgements 

<p align = "center"><img src = "https://media.giphy.com/media/1gQ6f5kJdBtGPSmdgS/giphy.gif" height = 300 alt = "Acknowledgment Icon"></p>


- **General Purpose Speech Recognition Model**: [OpenAI Whisper](https://openai.com/blog/whisper/) 
    - [GitHub](https://github.com/openai/whisper)
    - [Paper:Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/pdf/2212.04356.pdf)
- **Animations**: [LottieFiles](https://lottiefiles.com)
- **Favicon**: [PNG Repo](https://www.pngrepo.com/svg/235200/artificial-intelligence-brain)
- **Sample Test Clip 1**: [" Thinkin About It "](https://pixabay.com/music/soft-house-setze-thinkin-about-you-radio-edit-129282/) by [Niklas Setzkorn](https://pixabay.com/users/setze-32054623/) </a> from [Pixabay](https://pixabay.com/)

