import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_engine():
    db_user = os.environ['MLB_DATA_USER']
    db_pw = os.environ['MLB_DATA_PW']
    db_ip = os.environ['MLB_DATA_IP']
    return create_engine(f'postgresql+psycopg2://{db_user}:{db_pw}@{db_ip}/baseball', echo=False)


def get_session():
    engine = get_engine()
    session = scoped_session(
        sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=engine
        )
    )

    return session
