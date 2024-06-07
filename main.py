from services.message_consumer import consume_message
from utility.database import get_engine, get_session

if __name__ == "__main__":
    print("[INFO] mlb-data-analyzer is running")
    # consume_message()
    engine = get_engine()
    session = get_session()
    consume_message(engine, session)
