# Libs
import os
import nltk
import spacy
from nltk.sentiment import SentimentIntensityAnalyzer

# Carregar modelo de linguagem em português
# python -m spacy download pt_core_news_sm

nlp = spacy.load("pt_core_news_sm")
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
    try:
        for tweet in os.listdir(path):
            with open(os.path.join(path, tweet), "r", encoding="utf-8") as text_file:
                text_content = text_file.read()
                files[tweet] = text_content
    except FileNotFoundError:
        print("Diretorio não encontrado ou não possui nenhum arquivo")
    return files

def extract_entities(text):
     """
    Extract named entities (locations and persons) from text.

    Args:
        text (str): Input text.

    Returns:
        list: List of tuples containing entity text and entity label.
    """
     doc = nlp(text)
     entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ["LOC", "PER"]]

     return entities

def analyze_entities(path):
    """
    Analyzes named entities in all files in a directory using spaCy.

    Args:
        path (str): Path to the directory containing the files.
    """
    files = read_files(path)
    if files:
        for filename, content in files.items():
            print(f"Entidades em {filename}:")
            for sentence in nltk.sent_tokenize(content):
                entities = extract_entities(sentence)
                locations = [entity[0] for entity in entities if entity[1] == "LOC"]
                persons = [entity[0] for entity in entities if entity[1] == "PER"]
                if locations:
                    print(f"Possiveis localizações: {locations}")
                if persons:
                    print(f"Possiveis entidades responsáveis: {persons}")

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
    analyze_entities(path)


# ================ Main code ==============

# Path with tweets
path = "assets/tweets"

if __name__ == "__main__":
    main(path)