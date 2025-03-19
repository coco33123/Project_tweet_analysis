import datetime
from config import BLACKLIST_USERS, KEYWORDS

# Définir la limite de date (30 jours)
DATE_LIMIT = datetime.datetime.now() - datetime.timedelta(days=30)

def filter_tweets(tweets_data):
    ignored_tweets = []
    filtered_tweets = []

    for entry in tweets_data:
        user, tweet, date = entry["user"], entry["tweet"].strip().lower(), entry["date"]

        # Vérifier blacklist
        if user in BLACKLIST_USERS:
            ignored_tweets.append(f"❌ {user} → {tweet} (Blacklist)")
            continue  

        # Vérifier mots-clés
        if not any(keyword in tweet for keyword in KEYWORDS):
            ignored_tweets.append(f"🚫 {user} → {tweet} (Pas pertinent)")
            continue  

        # Vérifier date récente
        if date < DATE_LIMIT:
            ignored_tweets.append(f"📅 {user} → {tweet} (Trop ancien)")
            continue  

        filtered_tweets.append({"user": user, "tweet": tweet, "date": date})

    return ignored_tweets, filtered_tweets