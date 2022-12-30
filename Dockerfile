# Use the official lightweight Python image
FROM python:3.9.16-slim-bullseye
# Add your application code and dependencies
ADD . /app
WORKDIR /app
# Install ffmpeg, git and other dependencies for Whisper
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*
# Update pip and install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the application code from source to destination inside container
COPY . .
# Expose port 8501
EXPOSE 8501
# Launch app when container is run
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]