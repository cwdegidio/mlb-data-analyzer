from services.message_consumer import consume_message
from utility.database import get_engine, get_session
from flask import Flask, jsonify
import threading
import time


class SharedData:
    def __init__(self):
        self.execution_time = 0


shared_data = SharedData()
app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    status = {
        "status": "ok",
    }
    return jsonify(status)

@app.route("/metrics", methods=["GET"])
def metrics():
    metrics = {
        "execution_time": shared_data.execution_time,
    }
    return jsonify(metrics)


if __name__ == "__main__":
    print("[INFO] mlb-data-analyzer is running")
    engine = get_engine()
    session = get_session()
    consumer = threading.Thread(target=consume_message, args=(engine, session, shared_data,), daemon=True)
    consumer.start()
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[INFO] Shutting down...")
