import speech_recognition as sr

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    
    # Check if the file is in a supported format
    if file_path.lower().endswith(('.wav', '.flac', '.aiff')):
        audio_file = sr.AudioFile(file_path)
    else:
        # Convert MP3 to WAV if necessary
        import moviepy.editor as mp
        mp.AudioFileClip(file_path).write_audiofile("temp.wav")
        audio_file = sr.AudioFile("temp.wav")

    with audio_file as source:
        audio_data = recognizer.record(source)
    
    try:
        return recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio"
    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service"
