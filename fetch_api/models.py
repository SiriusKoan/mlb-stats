from sqlalchemy import Date, Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class Teams(base):
    __tablename__ = "teams"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    fullname = Column(String, unique=True, nullable=False)
    abbreviation = Column(String, unique=True, nullable=False)
    location = Column(String, nullable=False)
    league = Column(String, nullable=False)
    division = Column(String, nullable=False)

    def __init__(self, id, name, fullname, abbreviation, location, league, division):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.abbreviation = abbreviation
        self.location = location
        self.league = league
        self.division = division


class Standings(base):
    __tablename__ = "standings"
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    date = Column(Date, nullable=False, index=True)
    # standard
    win = Column(Integer, nullable=False, default=0)
    loss = Column(Integer, nullable=False, default=0)
    division_rank = Column(Integer, nullable=False, default=0)
    league_rank = Column(Integer, nullable=False, default=0)
    GB = Column(
        Float, nullable=False, default=0.0
    )  # GB = games behind, the first place has 0 games behind
    WCGB = Column(Float, nullable=False, default=0.0)  # WCGB = wild card games behind
    XTRA_win = Column(Integer, nullable=False, default=0)  # XTRA = extra innings
    XTRA_loss = Column(Integer, nullable=False, default=0)
    RS = Column(Integer, nullable=False, default=0)  # RS = runs scored
    RA = Column(Integer, nullable=False, default=0)  # RA = runs allowed
    home_win = Column(Integer, nullable=False, default=0)
    home_loss = Column(Integer, nullable=False, default=0)
    away_win = Column(Integer, nullable=False, default=0)
    away_loss = Column(Integer, nullable=False, default=0)
    vs_500_win = Column(Integer, nullable=False, default=0)  # vs. >.500 teams
    vs_500_loss = Column(Integer, nullable=False, default=0)
    # advanced
    one_run_win = Column(
        Integer, nullable=False, default=0
    )  # 1-run game: win or lose by 1 run
    one_run_loss = Column(Integer, nullable=False, default=0)
    day_games_win = Column(Integer, nullable=False, default=0)
    day_games_loss = Column(Integer, nullable=False, default=0)
    night_games_win = Column(Integer, nullable=False, default=0)
    night_games_loss = Column(Integer, nullable=False, default=0)
    grass_games_win = Column(Integer, nullable=False, default=0)  # grass: natural grass
    grass_games_loss = Column(Integer, nullable=False, default=0)
    turf_games_win = Column(Integer, nullable=False, default=0)  # turf: artificial turf
    turf_games_loss = Column(Integer, nullable=False, default=0)
    vs_east_win = Column(Integer, nullable=False, default=0)  # vs. east
    vs_east_loss = Column(Integer, nullable=False, default=0)
    vs_central_win = Column(Integer, nullable=False, default=0)  # vs. central
    vs_central_loss = Column(Integer, nullable=False, default=0)
    vs_west_win = Column(Integer, nullable=False, default=0)  # vs. west
    vs_west_loss = Column(Integer, nullable=False, default=0)
    vs_interleague_win = Column(Integer, nullable=False, default=0)  # vs. interleague
    vs_interleague_loss = Column(Integer, nullable=False, default=0)
    vs_R_win = Column(
        Integer, nullable=False, default=0
    )  # vs. right-handed starting pitchers
    vs_R_loss = Column(Integer, nullable=False, default=0)
    vs_L_win = Column(
        Integer, nullable=False, default=0
    )  # vs. left-handed starting pitchers
    vs_L_loss = Column(Integer, nullable=False, default=0)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
