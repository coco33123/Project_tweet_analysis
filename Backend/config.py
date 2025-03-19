import os

# RabbitMQ Configuration
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))

# Exchange pour Pub/Sub
EXCHANGE_NAME = "tweet_sentiment_exchange"

# Sentiment topics
TOPICS = ["positif", "neutre", "négatif"]

# Filtres
BLACKLIST_USERS = ["Bot123", "FakeNewsUser", "SpamAccount"]
KEYWORDS = ["produit", "service", "publicité", "marketing", "prix", "achat"]
DAYS_LIMIT = 30  # Seuls les tweets récents sont pris en compte

# Fichiers de stockage
DATA_DIR = "data"
TWEETS_FILE = os.path.join(DATA_DIR, "tweets.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
