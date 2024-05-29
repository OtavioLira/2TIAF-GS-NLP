import os
from nltk.sentiment import SentimentIntensityAnalyzer

# Uncomment the following line if you haven't downloaded the Vader lexicon yet
# import nltk
# nltk.download("vader_lexicon")

def read_files(path):
    """
    Reads all files in a directory and returns a dictionary with filenames as keys and their content as values.

    Args:
        path (str): Path to the directory containing the files.

    Returns:
        dict: Dictionary mapping filenames to their content.
    """
    files = {}
    try:
        for tweet in os.listdir(path):
            with open(os.path.join(path, tweet), "r", encoding="utf-8") as text_file:
                text_content = text_file.read()
                files[tweet] = text_content
    except FileNotFoundError:
        print("Directory not found or does not contain any files.")
    return files


def analyze_sentiment(path):
    """
    Analyzes sentiment of all files in a directory using Vader lexicon.

    Args:
        path (str): Path to the directory containing the files.
    """
    analyzer = SentimentIntensityAnalyzer()
    files = read_files(path)
    if files:
        for filename, content in files.items():
            scores = analyzer.polarity_scores(content)
            print(f"Text: {filename}\n Scores: {scores}")


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

if __name__ == "__main__":
    main(path)
