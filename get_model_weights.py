import os
import urllib.request
from tqdm import tqdm

# URLs of the model weights files
urls = [
"https://openaipublic.azureedge.net/main/whisper/models/65147644a518d12f04e32d6f3b26facc3f8dd46e5390956a9424a650c0ce22b9/tiny.pt",
 "https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt", 
 "https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt",
 "https://openaipublic.azureedge.net/main/whisper/models/81f7c96c852ee8fc832187b0132e569d6c3065a3252ed18e56effd0b6a73e524/large-v2.pt"]

# Create the 'models' sub-directory if it does not exist
if not os.path.exists('./assets/models'):
    os.makedirs('./assets/models')

# Download the model weights files
for url in tqdm(urls, desc='Downloading Whisper Model Weights'):
    file_name = url.split('/')[-1]
    print(f"Going for {url.split('.')[0]} model")
    urllib.request.urlretrieve(url, file_path)