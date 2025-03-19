import pika
import json
from config import RABBITMQ_HOST, EXCHANGE_NAME

def publish_message(sentiment, tweets):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    # Déclare l'échange en mode FANOUT
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')

    # Création du message JSON
    message_body = json.dumps({"sentiment": sentiment, "tweets": tweets})
    
    # Envoi du message
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key='', body=message_body)
    print(f"📤 Envoyé dans [{sentiment}] → {len(tweets)} tweets agrégés.\n")

    connection.close()

if __name__ == "__main__":
    # Envoi des tweets par catégorie
    publish_message("positif", ["J'adore ce produit!", "Super service client!"])
    publish_message("neutre", ["C'est un produit correct.", "Prix raisonnable."])
    publish_message("négatif", ["Produit défectueux!", "Trop cher pour la qualité."])
    
    print("✅ Un seul message par sentiment a été publié dans les topics correspondants.")
