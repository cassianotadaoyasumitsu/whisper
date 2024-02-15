import whisper

# Load the base model
model = whisper.load_model("base")
audio = "audio.mp3"
result = model.transcribe(audio)
print(result["text"])

# Write the transcription text to a .txt file
with open(f"{audio}.txt", "w") as file:
    file.write(result["text"])

# Print the path to the .txt file
print(f"Transcription saved to {audio}.txt")
