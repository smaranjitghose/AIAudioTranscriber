# Use the official lightweight Python image
FROM python:3.9-slim
# Expose port 
ENV PORT 8501
# Setting our working directory to .app
WORKDIR /app
ADD . /app
# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
# Install ffmpeg
RUN apt install ffmpeg
# Install code dependencies
RUN pip install -r requirements.txt
# Copying all files over
COPY . /app
# Launch app when container is run
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]