import speech_recognition as sr

def recognize_speech(recognizer_instance):
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer_instance.listen(source, timeout=10, phrase_time_limit=5)
            text = recognizer_instance.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
    except sr.UnknownValueError:
        print("Error: Could not understand the audio.")
        return "I couldn't understand you."
    except sr.RequestError as e:
        print(f"Error: API request failed with error: {e}")
        return "API error occurred."
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "An unexpected error occurred."
