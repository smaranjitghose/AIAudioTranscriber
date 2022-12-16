## AI Audio Transcriber

<p align = "center"><img src = "./assets/transcriber.gif" height = 300 alt = "Wallet Icon"></p>

A minimalistic application to generate transcriptions for audio built using Python



## Set-Up ⚒️

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

## Demo

**v.0.0.1*
<p align = "center"><img src = "./assets/demo_snapshot_v1.png" height = 300 alt = "Hosting Icon"></p>


## Deployment Options 🥊

<p align = "center"><img src = "./assets/hosting.gif" height = 300 alt = "Hosting Icon"></p>

**Free Tier**
- [Streamlit Cloud](https://streamlit.io/cloud)  ✔️
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [Fly](https://fly.io/)
- [Cyclic](https://app.cyclic.sh/#/)

**No Free Tier**
- [Heroku](https://www.heroku.com/)
- [Digital Ocean](https://www.digitalocean.com/)

## Note ✏️

<p align = "center"><img src = "./assets/notes.gif" height = 300 alt = "SetUp Icon"></p>

- For Streamlit Sharing, mentioning versions of the modules in requirements throws error at times
- Large Modelv2 outperforms all other versions of Whisper in terms of performance especially in Multi-lingual Transcription. However, it takes a 10 times more V-RAM than the base model and has longer inference time



## Acknowledgements 🙏

<p align = "center"><img src = "https://media.giphy.com/media/1gQ6f5kJdBtGPSmdgS/giphy.gif" height = 300 alt = "Acknowledgment Icon"></p>


- **General Purpose Speech Recognition Model**: [OpenAI Whisper](https://openai.com/blog/whisper/) 
    - [GitHub](https://github.com/openai/whisper)
    - [Paper:Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/pdf/2212.04356.pdf)
- **Animations**: [LottieFiles](https://lottiefiles.com)
- **Sample Test Clip 1**: [" Thinkin About It "](https://pixabay.com/music/soft-house-setze-thinkin-about-you-radio-edit-129282/) by [Niklas Setzkorn](https://pixabay.com/users/setze-32054623/) </a> from [Pixabay](https://pixabay.com/)