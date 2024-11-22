from modules.speech_recognition import recognize_speech
from modules.emotion_detection import detect_emotion_vader
from modules.text_to_speech import speak
from modules.emotion_detection_camera import detect_emotion_camera
import nltk
nltk.download('punkt')  # Example: download the Punkt tokenizer
nltk.download('vader_lexicon')  # If you're using VADER for sentiment analysis

def main():
    print("Starting Emotion-Based Assistant...")
    print("Choose an input method:")
    print("1. Text-based Emotion Detection")
    print("2. Live Camera Emotion Detection")
    print("Say 'exit' or 'quit' to stop the program.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("Text-based emotion detection selected.")
        while True:
            print("\nListening...")
            try:
                user_input = recognize_speech()
                if user_input.lower() in ['exit', 'quit']:
                    print("Exiting... Goodbye!")
                    break

                print(f"Recognized: {user_input}")
                emotion = detect_emotion_vader(user_input)
                print(f"Detected Emotion: {emotion}")

                # Generate a response based on emotion
                if emotion == "positive":
                    response = "You seem happy! How can I assist you further?"
                elif emotion == "negative":
                    response = "I'm here for you. Please tell me how I can help."
                else:
                    response = "I'm here to listen, no matter how you're feeling!"

                print(f"Assistant: {response}")
                speak(response)

            except Exception as e:
                print(f"Error: {str(e)}")
                speak("Sorry, something went wrong.")

    elif choice == "2":
        print("Starting live camera emotion detection...")
        detect_emotion_camera()

    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
