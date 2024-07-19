import time
from sqlalchemy import text


def set_ops_batting_leaders(engine, session, shared_data):
    start = time.time()

    query_result = text("""
        DROP TABLE IF EXISTS ops_leaders;
        CREATE TABLE IF NOT EXISTS ops_leaders (
            id INTEGER PRIMARY KEY,
            player_id VARCHAR(10),
            team VARCHAR(3),
            first_name VARCHAR(80),
            last_name VARCHAR(80),
            bats VARCHAR(1),
            games_played INTEGER,
            plate_appearances INTEGER,
            team_games_played INTEGER,
            app_per_game NUMERIC,
            at_bats INTEGER,
            batting_average NUMERIC,
            on_base_plus_slugging NUMERIC
        );
        INSERT INTO ops_leaders (
            id, player_id, team, first_name, last_name, bats,
            games_played, plate_appearances, team_games_played, app_per_game, at_bats, batting_average, on_base_plus_slugging
        )
        SELECT
            players.id,
            players.player_id,
            standings.short_name,
            players.first_name,
            players.last_name,
            players.bats,
            batting.games_played,
            batting.plate_appearances,
            standings.total_games,
            (batting.plate_appearances::numeric / standings.total_games::numeric) AS app_per_game,           
            batting.at_bats,
            batting.batting_average,
            batting.on_base_plus_slugging
        FROM players
        INNER JOIN batting
            ON batting.first_name = players.first_name AND batting.last_name = players.last_name
        INNER JOIN standings
            ON standings.short_name = players.team
        WHERE (batting.plate_appearances::numeric / standings.total_games::numeric) >= 3.1
        ORDER BY batting.on_base_plus_slugging DESC;
    """)

    try:
        session.execute(query_result)
        session.commit()
        print("[INFO] Top batters by On-Base + Slugging (OPS) calculated.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

    end = time.time()
    print(f"[INFO] Execution time: {end - start:.2f} seconds")
    shared_data.execution_time = end - start
