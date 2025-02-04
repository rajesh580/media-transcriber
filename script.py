import os
import json
import whisper
from pathlib import Path

model = whisper.load_model("tiny")

def find_media_files(directory):
    media_extensions = {".mp3", ".wav", ".mp4", ".m4a", ".ogg", ".flac", ".mov", ".avi", ".mkv"}
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if Path(file).suffix.lower() in media_extensions:
                media_files.append(os.path.join(root, file))
    return media_files

def transcribe_media(file_path):
    try:
        result = model.transcribe(file_path)
        return result["text"].strip()
    except Exception as e:
        print(f"Error transcribing {file_path}: {e}")
        return None

def save_transcription(file_path, transcription, output_folder):
    if transcription:
        output_path = os.path.join(output_folder, Path(file_path).stem + ".json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump({"file": file_path, "transcription": transcription}, f, indent=4)
        print(f"Saved transcription: {output_path}")

def process_directory(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    media_files = find_media_files(input_folder)
    print(f"Found {len(media_files)} media files.")
    
    for media_file in media_files:
        print(f"Processing: {media_file}")
        transcription = transcribe_media(media_file)
        save_transcription(media_file, transcription, output_folder)
    
    print("Processing complete.")

if __name__ == "__main__":
    input_folder = "media_files" 
    output_folder = "transcriptions"
    process_directory(input_folder, output_folder)