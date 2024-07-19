import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def get_test_engine():
    db_user = os.environ['MLB_DATA_USER']
    db_pw = os.environ['MLB_DATA_PW']
    db_ip = os.environ['MLB_DATA_IP']
    # db_user = 'data_collector'
    # db_pw = 'testing1234'
    # db_ip = '66.228.48.112:8001'
    return create_engine(f'postgresql+psycopg2://{db_user}:{db_pw}@{db_ip}/test_baseball', echo=False)


def get_test_session():
    engine = get_test_engine()
    session = scoped_session(
        sessionmaker(
            autoflush=False,
            autocommit=False,
            bind=engine
        )
    )

    return session
