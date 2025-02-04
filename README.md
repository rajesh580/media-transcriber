# Media Transcriber

A Python script that scans a directory for media files (audio/video), transcribes them using OpenAI Whisper, and saves the transcription in JSON format.

## Features
- Recursively scans folders for media files (MP3, WAV, MP4, etc.)
- Uses OpenAI's Whisper (tiny model) for transcription
- Saves transcription results in JSON format

## Requirements
Ensure you have the following installed:

- Python 3.8+
- OpenAI Whisper
- ffmpeg

### Install dependencies
```sh
pip install openai-whisper ffmpeg-python
```

### Install ffmpeg
#### Windows
```sh
choco install ffmpeg
```
#### Linux (Ubuntu/Debian)
```sh
sudo apt install ffmpeg
```
#### macOS
```sh
brew install ffmpeg
```

## Usage
```sh
python media_transcriber.py
```

## How It Works
1. Scans the `media_files` directory for media files
2. Transcribes each file using Whisper
3. Saves the transcriptions as JSON in the `transcriptions` folder

## Example Output
A sample transcription JSON file:
```json
{
  "file": "media_files/example.mp4",
  "transcription": "Hello, this is a test transcription."
}
```

## Contributing
Feel free to fork this repository and submit pull requests!
