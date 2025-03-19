import datetime
from config import BLACKLIST_USERS, KEYWORDS

# Définir la limite de date (30 jours)
DATE_LIMIT = datetime.datetime.now() - datetime.timedelta(days=30)

def filter_tweets(tweets_data):
    ignored_tweets = []
    filtered_tweets = []

    for entry in tweets_data:
        user = entry["user"]
        tweet = entry["tweet"].strip().lower()
        raw_date = entry["date"]

        # Convertir la date ISO string → datetime
        try:
            tweet_date = datetime.datetime.fromisoformat(raw_date)
        except ValueError:
            ignored_tweets.append(f"⚠️ {user} → {tweet} (Date invalide)")
            continue

        # Vérifier blacklist
        if user in BLACKLIST_USERS:
            ignored_tweets.append(f"❌ {user} → {tweet} (Blacklist)")
            continue  

        # Vérifier mots-clés
        if not any(keyword in tweet for keyword in KEYWORDS):
            ignored_tweets.append(f"🚫 {user} → {tweet} (Pas pertinent)")
            continue  

        # Vérifier date récente (< 30 jours)
        if tweet_date < DATE_LIMIT:
            ignored_tweets.append(f"📅 {user} → {tweet} (Trop ancien)")
            continue 

        filtered_tweets.append({"user": user, "tweet": tweet, "date": raw_date})

    return ignored_tweets, filtered_tweets
