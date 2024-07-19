from sqlalchemy import Column, Integer, String, Numeric
from models.base import TimeStampedModel

class OpsLeaderDB(TimeStampedModel):
    __tablename__ = 'ops_leaders'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    player_id = Column('player_id', String(10))
    team = Column('team', String(3))
    first_name = Column('first_name', String(80))
    last_name = Column('last_name', String(80))
    bats = Column('bats', String(1))
    games_played = Column('games_played', Integer)
    plate_appearances = Column('plate_appearances', Integer)
    team_games_played = Column('team_games_played', Integer)
    app_per_game = Column('app_per_game', Numeric)
    at_bats = Column('at_bats', Integer)
    batting_average = Column('batting_average', Numeric)
    on_base_plus_slugging = Column('on_base_plus_slugging', Numeric)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.first_name}, {self.last_name})'
