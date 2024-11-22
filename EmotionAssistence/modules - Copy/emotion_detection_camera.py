import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

# Load the pre-trained emotion detection model
emotion_model_path = "models/emotion_model.h5"  # Update with your model's path
emotion_classifier = load_model(emotion_model_path, compile=False)

# Emotion categories
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def detect_emotion_camera():
    # Start webcam feed
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale (required by most emotion models)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            roi_gray = gray_frame[y:y+h, x:x+w]  # Region of Interest (face area)
            roi_gray = cv2.resize(roi_gray, (48, 48))  # Resize to match model input
            roi_gray = roi_gray.astype("float") / 255.0
            roi_gray = img_to_array(roi_gray)
            roi_gray = np.expand_dims(roi_gray, axis=0)

            # Predict emotion
            prediction = emotion_classifier.predict(roi_gray)
            max_index = np.argmax(prediction)
            emotion = emotion_labels[max_index]

            # Draw rectangle around face and label with emotion
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Emotion Detector', frame)

        # Break loop with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
