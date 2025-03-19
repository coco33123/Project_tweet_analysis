import pika
import json
import sys
from config import RABBITMQ_HOST, EXCHANGE_NAME

def callback(ch, method, properties, body):
    message = json.loads(body)
    sentiment = message["sentiment"]
    tweets = message["tweets"]
    print(f"📩 Message reçu sur [{sentiment}] → {tweets}")

def subscribe():
    if len(sys.argv) < 2:
        print("Usage: python pubsub_subscriber.py <sentiment>")
        return
    
    topic = sys.argv[1]  # Exemple: "positif"

    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    # Déclare l'échange en mode FANOUT
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='fanout')

    # Création d'une file temporaire pour recevoir les messages
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Liaison de la file à l'échange
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name)

    print(f"📬 En attente de messages sur [{topic}]... (CTRL+C pour arrêter)")
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

if __name__ == "__main__":
    subscribe()
