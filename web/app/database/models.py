from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Teams(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, unique=True, nullable=False)
    abbreviation = db.Column(db.String, unique=True, nullable=False)
    location = db.Column(db.String, nullable=False)
    league = db.Column(db.String, nullable=False)
    division = db.Column(db.String, nullable=False)

    def __init__(self, id, name, fullname, abbreviation, location, league, division):
        self.id = id
        self.name = name
        self.fullname = fullname
        self.abbreviation = abbreviation
        self.location = location
        self.league = league
        self.division = division


class Standing(db.Model):
    __tablename__ = "standing"
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    # standard
    win = db.Column(db.Integer, nullable=False, default=0)
    loss = db.Column(db.Integer, nullable=False, default=0)
    GB = db.Column(
        db.Float, nullable=False, default=0.0
    )  # GB = games behind, the first place has 0 games behind
    WCGB = db.Column(
        db.Float, nullable=False, default=0.0
    )  # WCGB = wild card games behind
    XTRA_win = db.Column(db.Integer, nullable=False, default=0)  # XTRA = extra innings
    XTRA_loss = db.Column(db.Integer, nullable=False, default=0)
    RS = db.Column(db.Integer, nullable=False, default=0)  # RS = runs scored
    RA = db.Column(db.Integer, nullable=False, default=0)  # RA = runs allowed
    home_win = db.Column(db.Integer, nullable=False, default=0)
    home_loss = db.Column(db.Integer, nullable=False, default=0)
    away_win = db.Column(db.Integer, nullable=False, default=0)
    away_loss = db.Column(db.Integer, nullable=False, default=0)
    vs_500_win = db.Column(db.Integer, nullable=False, default=0)  # vs. >.500 teams
    vs_500_loss = db.Column(db.Integer, nullable=False, default=0)
    # advanced
    one_run_win = db.Column(
        db.Integer, nullable=False, default=0
    )  # 1-run game: win or lose by 1 run
    one_run_loss = db.Column(db.Integer, nullable=False, default=0)
    day_games_win = db.Column(db.Integer, nullable=False, default=0)
    day_games_loss = db.Column(db.Integer, nullable=False, default=0)
    night_games_win = db.Column(db.Integer, nullable=False, default=0)
    night_games_loss = db.Column(db.Integer, nullable=False, default=0)
    grass_games_win = db.Column(
        db.Integer, nullable=False, default=0
    )  # grass: natural grass
    grass_games_loss = db.Column(db.Integer, nullable=False, default=0)
    turf_games_win = db.Column(
        db.Integer, nullable=False, default=0
    )  # turf: artificial turf
    turf_games_loss = db.Column(db.Integer, nullable=False, default=0)
    vs_east_win = db.Column(db.Integer, nullable=False, default=0)  # vs. east
    vs_east_loss = db.Column(db.Integer, nullable=False, default=0)
    vs_central_win = db.Column(db.Integer, nullable=False, default=0)  # vs. central
    vs_central_loss = db.Column(db.Integer, nullable=False, default=0)
    vs_west_win = db.Column(db.Integer, nullable=False, default=0)  # vs. west
    vs_west_loss = db.Column(db.Integer, nullable=False, default=0)
    vs_interleague_win = db.Column(
        db.Integer, nullable=False, default=0
    )  # vs. interleague
    vs_interleague_loss = db.Column(db.Integer, nullable=False, default=0)
    vs_R_win = db.Column(
        db.Integer, nullable=False, default=0
    )  # vs. right-handed starting pitchers
    vs_R_loss = db.Column(db.Integer, nullable=False, default=0)
    vs_L_win = db.Column(
        db.Integer, nullable=False, default=0
    )  # vs. left-handed starting pitchers
    vs_L_loss = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
