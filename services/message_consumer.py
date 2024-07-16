import pika
import json
import os
import functools
from services.set_avg_games import set_avg_games_played
from services.set_ops_leaders import set_ops_batting_leaders


def consume_message(engine, session, shared_data):
    url = os.environ["MLB_MQ_URL"]
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='mlb_data')

    def callback(channel, method, properties, body, shared_data):
        message_json = body.decode()
        message_dict = json.loads(message_json)
        print(f"[INFO] Message Received. Status: {message_dict["status"]}")
        if message_dict["status"] == "OK":
            set_avg_games_played(session)
            set_ops_batting_leaders(engine, session, shared_data)
        else:
            print("[ERROR] Non-OK message consumed.")
        print("[INFO] Waiting for new message. Press Ctrl + C to quit.")

    this_callback = functools.partial(callback, shared_data=(shared_data))
    channel.basic_consume(
        queue='mlb_data',
        on_message_callback=this_callback,
        auto_ack=True
    )

    channel.start_consuming()

