import pika
import json
from services.set_avg_games import set_avg_games_played
from services.set_ops_leaders import set_ops_batting_leaders


def consume_message(engine, session):
    url = "amqps://pohsouqu:xeOKC-H3Y3TU5rQezAqI_WIUxqOq9-mG@shrimp.rmq.cloudamqp.com/pohsouqu"
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def callback(channel, method, properties, body):
        message_json = body.decode()
        message_dict = json.loads(message_json)
        print(f"[INFO] Message Received. Status: {message_dict["status"]}")
        if message_dict["status"] == "OK":
            set_avg_games_played(session)
            set_ops_batting_leaders(engine, session)
        print("[INFO] Waiting for new message. Press Ctrl + C to quit.")

    channel.basic_consume(
        queue='hello',
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()

