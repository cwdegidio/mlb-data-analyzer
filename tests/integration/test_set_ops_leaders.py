import unittest
from models.base import Model
from models.ops_leaderdb import OpsLeaderDB
from tests.test_utility.database_test import get_test_engine, get_test_session
from tests.test_utility.populate_tables import populate_player_test_table, populate_batting_test_table, populate_standings_test_table
from services.set_ops_leaders import set_ops_batting_leaders

class SharedData:
    def __init__(self):
        self.execution_time = 0

class MyTestCase(unittest.TestCase):
    def test_set_ops_batting_leaders(self):
        shared_data = SharedData()

        engine = get_test_engine()
        session = get_test_session()

        populate_player_test_table(engine, session)
        populate_batting_test_table(engine, session)
        populate_standings_test_table(engine, session)

        set_ops_batting_leaders(engine, session, shared_data)

        count = session.query(OpsLeaderDB.id).count()

        session.close()

        self.assertEqual(count, 2)
