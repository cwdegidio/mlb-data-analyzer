from sqlalchemy import text


def set_avg_games_played(session):
    avg_query = text("""
        SELECT AVG(games_played) as avg_games_played
        FROM batting;
    """)

    result = session.execute(avg_query).scalar()

    insert_query = text("""
        CREATE TABLE IF NOT EXISTS avg_games_played (
            avg_games_result FLOAT
        );
        INSERT INTO avg_games_played (avg_games_result) VALUES (:avg_games_result);
    """)

    session.execute(insert_query, {'avg_games_result': result})
    session.commit()
    print("[INFO] Mean games played calculated.")
