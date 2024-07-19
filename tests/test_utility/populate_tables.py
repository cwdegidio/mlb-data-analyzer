from sqlalchemy import text


def populate_player_test_table(engine, session):
    query_result = text("""
        DROP TABLE IF EXISTS players;
        CREATE TABLE IF NOT EXISTS players(
            id INTEGER PRIMARY KEY,
            player_id VARCHAR(10),
            team VARCHAR(3),
            uniform_number VARCHAR,
            first_name VARCHAR(80) NOT NULL,
            last_name VARCHAR(80) NOT NULL,
            country VARCHAR(3) NOT NULL,
            position VARCHAR(15) NOT NULL,
            is_active BOOLEAN NOT NULL,
            age INTEGER NOT NULL,
            bats VARCHAR(1) NOT NULL,
            throws VARCHAR(1) NOT NULL,
            height VARCHAR(10) NOT NULL,
            weight INTEGER NOT NULL,
            dob VARCHAR(80) NOT NULL,
            first_year INTEGER NOT NULL
        );
        INSERT INTO players (
            id, player_id, team, uniform_number, first_name, last_name, country, position, is_active, age, bats, throws, height, weight, dob, first_year
        ) 
        VALUES
            (14, '14-ATL', 'ATL', '27', 'Austin', 'Riley', 'US', 'Position', true,  27, 'R', 'R', '6'' 3"', 240, 'Apr 2, 1997', 2015),
            (243, '25-NYY', 'NYY', '99', 'Aaron', 'Judge', 'US', 'Position', true,  32, 'R', 'R', '6'' 7"', 282, 'Apr 26, 1992', 2011),
            (680, '18-CLE', 'CLE', '6', 'David', 'Fry', 'US', 'Position', true,  28, 'R', 'R', '6'' 0"', 215, 'Nov 20, 1995', 2015);
    """)

    try:
        session.execute(query_result)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

    print("[INFO] Players (test) table created.")


def populate_batting_test_table(engine, session):
    query_result = text("""
        DROP TABLE IF EXISTS batting;
        CREATE TABLE IF NOT EXISTS batting(
            id INTEGER PRIMARY KEY,
            first_name VARCHAR(80) NOT NULL,
            last_name VARCHAR(80) NOT NULL,
            games_played INTEGER,
            plate_appearances INTEGER,
            at_bats INTEGER,
            runs INTEGER,
            hits INTEGER,
            doubles INTEGER,
            triples INTEGER,
            home_runs INTEGER,
            runs_batted_in INTEGER,
            stolen_bases INTEGER,
            caught_stealing INTEGER,
            base_on_balls INTEGER,
            strikeouts NUMERIC,
            batting_average NUMERIC,
            on_base_percentage NUMERIC,
            slugging_percentage NUMERIC,
            on_base_plus_slugging NUMERIC
        );
        INSERT INTO batting (
            id, first_name, last_name, games_played, plate_appearances, at_bats, runs, hits, doubles, triples, home_runs, runs_batted_in, stolen_bases, caught_stealing, base_on_balls, strikeouts, batting_average, on_base_percentage, slugging_percentage, on_base_plus_slugging
        ) 
        VALUES
            (5, 'Austin', 'Riley', 82, 347, 311, 48, 80, 20, 2, 12, 39, 0, 0, 31,87, 0.257, 0.329, 0.45, 0.779),
            (106, 'Aaron', 'Judge', 96, 424, 343, 73, 105, 24, 1, 34, 85, 5, 0, 72, 106, 0.306, 0.433, 0.679, 1.112),
            (307, 'David' , 'Fry', 73, 246, 204, 29, 57, 14, 0, 8, 33, 4, 1, 30, 50, 0.279, 0.388, 0.466, 0.853);
    """)

    try:
        session.execute(query_result)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

    print("[INFO] Batting (test) table created.")


def populate_standings_test_table(engine, session):
    query_result = text(""" 
        DROP TABLE IF EXISTS standings;
        CREATE TABLE IF NOT EXISTS standings(
            id INTEGER PRIMARY KEY,
            team VARCHAR(80),
            short_name VARCHAR(3),
            wins INTEGER,
            losses INTEGER,
            total_games INTEGER
        );
        INSERT INTO standings (
            id, team, short_name, wins, losses, total_games
        ) 
        VALUES
            (8, 'Atlanta Braves', 'ATL', 53, 42, 95),
            (4, 'New York Yankees', 'NYY', 58, 40, 98),
            (2, 'Cleveland Guardians', 'CLE', 58, 37, 95);
    """)

    try:
        session.execute(query_result)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

    print("[INFO] Standings (test) table created.")
