import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import ssl

# Uses default sentiment analyzer 
sia = SentimentIntensityAnalyzer()

# Testing NLP
print(sia.polarity_scores("Wow, NLTK is really powerful!"))
print(sia.polarity_scores("I hate cars. Some cars just break down everytime I use them."))
print(sia.polarity_scores("I love Burger Co. They have the best bacon cheese tater tots."))


def sentimentAnalyzer(text):
    """
    This function runs the sentiment intensity analyzer from
    the nltk module. It returns the compound score from the 
    analysis.

    Parameters:
    -------------
    text : str
        A string of text to analyze the sentiment

    Returns:
    score : float
        A float (from -1 to 1) representing the sentiment of the text

    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text)["compound"]