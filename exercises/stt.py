import vosk
import wave

# Load the Vosk model for English
model = vosk.Model(lang="en")

# Initialize the recognizer with the model and sample rate (16000 Hz for common audio files)
recognizer = vosk.KaldiRecognizer(model, 16000)

# Sample audio file for recognition
audio_file = "en.wav"  # Replace with the path to your audio file

# Open the audio file
with wave.open(audio_file, "rb") as audio:
    # Check if the file is mono and has the correct sample rate
    if audio.getnchannels() != 1 or audio.getframerate() != 16000:
        raise ValueError("Audio file must be mono and 16kHz")
    
    # Read the audio data in chunks
    while True:
        data = audio.readframes(4000)
        if len(data) == 0:
            break
        
        # Recognize the speech in the chunk
        if recognizer.AcceptWaveform(data):
            print(recognizer.Result())  # Print recognized text for the current chunk
        else:
            print(recognizer.PartialResult())  # Print partial result for ongoing recognition

# Get the final recognized result
result = recognizer.FinalResult()
print("Final Result:", result)  # Print the complete transcription

