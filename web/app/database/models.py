from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Teams(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    fullname = db.Column(db.String, unique=True, nullable=False)
    location = db.Column(db.String, nullable=False)
    league = db.Column(db.String, nullable=False)
    division = db.Column(db.String, nullable=False)


class Standing(db.Model):
    __tablename__ = "standing"
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    # standard
    win = db.Column(db.Integer, nullable=False)
    loss = db.Column(db.Integer, nullable=False)
    GB = db.Column(
        db.Integer, nullable=False
    )  # GB = games behind, the first place has 0 games behind
    WCGB = db.Column(db.Integer, nullable=False)  # WCGB = wild card games behind
    XTRA_win = db.Column(db.Integer, nullable=False)  # XTRA = extra innings
    XTRA_loss = db.Column(db.Integer, nullable=False)
    RS = db.Column(db.Integer, nullable=False)  # RS = runs scored
    RA = db.Column(db.Integer, nullable=False)  # RA = runs allowed
    home_win = db.Column(db.Integer, nullable=False)
    home_loss = db.Column(db.Integer, nullable=False)
    away_win = db.Column(db.Integer, nullable=False)
    away_loss = db.Column(db.Integer, nullable=False)
    vs_500_win = db.Column(db.Integer, nullable=False)  # vs. >.500 teams
    vs_500_loss = db.Column(db.Integer, nullable=False)
    # advanced
    one_run_win = db.Column(
        db.Integer, nullable=False
    )  # 1-run game: win or lose by 1 run
    one_run_loss = db.Column(db.Integer, nullable=False)
    day_games_win = db.Column(db.Integer, nullable=False)
    day_games_loss = db.Column(db.Integer, nullable=False)
    night_games_win = db.Column(db.Integer, nullable=False)
    night_games_loss = db.Column(db.Integer, nullable=False)
    grass_games_win = db.Column(db.Integer, nullable=False)  # grass: natural grass
    grass_games_loss = db.Column(db.Integer, nullable=False)
    turf_games_win = db.Column(db.Integer, nullable=False)  # turf: artificial turf
    turf_games_loss = db.Column(db.Integer, nullable=False)
    vs_east_win = db.Column(db.Integer, nullable=False)  # vs. east
    vs_east_loss = db.Column(db.Integer, nullable=False)
    vs_central_win = db.Column(db.Integer, nullable=False)  # vs. central
    vs_central_loss = db.Column(db.Integer, nullable=False)
    vs_west_win = db.Column(db.Integer, nullable=False)  # vs. west
    vs_west_loss = db.Column(db.Integer, nullable=False)
    vs_interleague_win = db.Column(db.Integer, nullable=False)  # vs. interleague
    vs_interleague_loss = db.Column(db.Integer, nullable=False)
    vs_R_win = db.Column(db.Integer, nullable=False)  # vs. right-handed starting pitchers
    vs_R_loss = db.Column(db.Integer, nullable=False)
    vs_L_win = db.Column(db.Integer, nullable=False)  # vs. left-handed starting pitchers
    vs_L_loss = db.Column(db.Integer, nullable=False)
