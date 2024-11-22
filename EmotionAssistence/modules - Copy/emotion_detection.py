# emotion_detection.py

# Additional Notes:
# 1. Install NLTK library:
# Run this command to install the nltk library:
# pip install nltk

# 2. Download the VADER lexicon used by NLTK for sentiment analysis:
import nltk
nltk.download('vader_lexicon')  # This downloads the VADER lexicon needed for sentiment analysis

# 3. Testing the assistant with different emotional phrases:
# Try testing with sentences like:
# - "I'm feeling really great today!" (Expected Emotion: happy)
# - "I'm so sad about this." (Expected Emotion: sad)
# - "I'm just neutral." (Expected Emotion: neutral)

from nltk.sentiment import SentimentIntensityAnalyzer

def detect_emotion_vader(text):
    """
    Detects the emotion (happy, sad, neutral) based on VADER sentiment analysis.
    
    Parameters:
        text (str): The input text from the user.
        
    Returns:
        str: The detected emotion (happy, sad, neutral).
    """
    # Initialize the VADER sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Get sentiment scores for the input text
    sentiment_score = analyzer.polarity_scores(text)
    
    # Classify emotion based on compound score
    if sentiment_score['compound'] >= 0.05:
        return "happy"
    elif sentiment_score['compound'] <= -0.05:
        return "sad"
    else:
        return "neutral"
