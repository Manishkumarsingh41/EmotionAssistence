# utils/logger.py
from config.settings import LOG_FILE_PATH

def log_interaction(user_input, emotion, response):
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(f"User: {user_input}\nEmotion: {emotion}\nResponse: {response}\n\n")
