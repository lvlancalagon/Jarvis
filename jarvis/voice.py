from gtts import gTTS
import os

def speak(text, filename="response.mp3", lang='ru'):
    """
    Generates an MP3 file from text using Google Text-to-Speech.
    Note: Audio playback is not possible in this environment,
    but the file will be generated for the user to download/play.
    """
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        return True
    except Exception as e:
        print(f"Error in TTS: {e}")
        return False

if __name__ == "__main__":
    speak("Привет, я Джарвис. Чем я могу вам помочь?", "test_voice.mp3")
    print("Audio file 'test_voice.mp3' generated.")
