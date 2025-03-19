from transformers import pipeline
from config import SENTIMENTS

# Charger le modèle de sentiment
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiments(filtered_tweets):
    sentiment_counts = {"positif": 0, "neutre": 0, "négatif": 0}
    analyzed_tweets = []

    for entry in filtered_tweets:
        tweet = entry["tweet"]
        sentiment_result = sentiment_pipeline(tweet)[0]
        score = sentiment_result["label"]

        # Classification des sentiments
        if "1 star" in score:
            sentiment_label = "négatif"
        elif "2 stars" in score or "3 stars" in score:
            sentiment_label = "neutre"
        elif "4 stars" in score or "5 stars" in score:
            sentiment_label = "positif"

        sentiment_counts[sentiment_label] += 1
        analyzed_tweets.append({"user": entry["user"], "tweet": tweet, "sentiment": sentiment_label})

    return sentiment_counts, analyzed_tweets
