from sqlalchemy import text, Table, Column, Integer, String, Numeric, MetaData


def set_ops_batting_leaders(engine, session):
    metadata = MetaData()

    ops_leaders = Table(
        'ops_leaders',
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('player_id', String),
        Column('first_name', String),
        Column('last_name', String),
        Column('bats', String),
        Column('games_played', Integer),
        Column('plate_appearances', Integer),
        Column('app_per_game', Numeric),
        Column('at_bats', Integer),
        Column('batting_average', Numeric),
        Column('on_base_plus_slugging', Numeric)
    )
    query_result = text("""
        WITH avg_games_played AS (
            SELECT avg_games_result AS avg_games
            FROM avg_games_played
        )
        INSERT INTO ops_leaders (
            id, player_id, first_name, last_name, bats,
            games_played, plate_appearances, app_per_game, at_bats, batting_average, on_base_plus_slugging
        )
        SELECT
            players.id,
            players.player_id,
            players.first_name,
            players.last_name,
            players.bats,
            batting.games_played,
            batting.plate_appearances,
            (batting.plate_appearances::numeric / batting.games_played::numeric) AS app_per_game,           
             batting.at_bats,
            batting.batting_average,
            batting.on_base_plus_slugging
        FROM players
        INNER JOIN batting
            ON batting.first_name = players.first_name
                   AND batting.last_name = players.last_name
        WHERE (batting.plate_appearances::numeric / batting.games_played::numeric) >= 3.1
          AND batting.games_played >= (SELECT avg_games FROM avg_games_played LIMIT 1)
        ORDER BY batting.on_base_plus_slugging DESC;
    """)

    metadata.create_all(engine)

    try:
        session.execute(query_result)
        session.commit()
        print("[INFO] Top batters by On-Base + Slugging (OPS) calculated.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()
