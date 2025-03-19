def aggregate_tweets(analyzed_tweets):
    aggregated = {"positif": [], "neutre": [], "négatif": []}

    for entry in analyzed_tweets:
        aggregated[entry["sentiment"]].append(entry["tweet"])

    # Sélectionner un seul message par sentiment (si au moins 3 tweets)
    messages_to_publish = []
    for sentiment, tweets in aggregated.items():
        if len(tweets) >= 3:
            messages_to_publish.append({"sentiment": sentiment, "tweets": tweets[:3]})  # Prend 3 tweets max

    return messages_to_publish
