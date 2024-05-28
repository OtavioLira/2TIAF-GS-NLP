# Libs
import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download Vader Lexicon (uncomment if not downloaded already)
# nltk.download("vader_lexicon")  # Uncomment this line to download

def read_files(path):
    """
    Reads all files in a directory and returns a dictionary with filenames as keys and their content as values.

    Args:
        path (str): Path to the directory containing the files.

    Returns:
        dict: Dictionary mapping filenames to their content.
    """
    files = {}
    for tweet in os.listdir(path):
        # Open file with proper encoding for text data
        with open(os.path.join(path, tweet), "r", encoding="utf-8") as text_file:
            # Read file content
            text_content = text_file.read()
            files[tweet] = text_content  # Use singular form for consistency
    return files


def analyze_sentiment(path):
    """
    Analyzes sentiment of all files in a directory using Vader lexicon.

    Args:
        path (str): Path to the directory containing the files.
    """
    # Load model (moved outside the loop for efficiency)
    analyzer = SentimentIntensityAnalyzer()

    # Analyze sentiment for each file
    for filename, content in read_files(path).items():
        scores = analyzer.polarity_scores(content)
        print(f"Text: {filename}\n Scores: {scores}")
        print(filename._.blob.sentiment_assessments.assessments)


def main(path):
    """
    Main function to call the sentiment analysis function.

    Args:
        path (str): Path to the directory containing the files.
    """
    analyze_sentiment(path)


# ================ Main code ==============

# Path with tweets
path = "assets/tweets"

main(path)
