def generate_response(input_text, emotion):
    """
    Generates a context-aware response based on user input and emotion.
    
    Parameters:
        input_text (str): The user's message.
        emotion (str): The detected emotion ('happy', 'sad', 'neutral').
        
    Returns:
        str: A crafted response.
    """
    if emotion == "happy":
        return f"That's fantastic! I'm glad to hear that. You mentioned: '{input_text}'"
    elif emotion == "sad":
        return "I'm sorry you're feeling this way. If there's anything I can do to help, let me know."
    elif emotion == "neutral":
        return f"I see. You mentioned: '{input_text}'. Tell me more if you'd like."
    else:
        return "I'm here to listen, no matter how you're feeling!"

# Example responses can be extended or modified for personalization.
