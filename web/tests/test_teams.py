import unittest
import datetime
from flask import url_for
from app import create_app
from app.database import db
from app.database.models import Teams, Standings


class BasicTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.team_data = {
            "id": 147,
            "name": "Yankees",
            "fullname": "New York Yankees",
            "abbreviation": "NYY",
            "location": "Bronx",
            "league": 103,
            "division": 201,
        }
        self.standing_data = {
            "team_id": 147,
            "date": datetime.datetime(2022, 6, 19, 0, 0),
            "win": 49,
            "loss": 16,
            "division_rank": "1",
            "league_rank": "1",
            "GB": 0.0,
            "WCGB": 0.0,
            "XTRA_win": 4,
            "XTRA_loss": 1,
            "RS": 331,
            "RA": 187,
            "home_win": 29,
            "home_loss": 7,
            "away_win": 20,
            "away_loss": 9,
            "vs_500_win": 20,
            "vs_500_loss": 7,
            "one_run_win": 14,
            "one_run_loss": 4,
            "day_games_win": 16,
            "day_games_loss": 7,
            "night_games_win": 33,
            "night_games_loss": 9,
            "grass_games_win": 43,
            "grass_games_loss": 13,
            "turf_games_win": 6,
            "turf_games_loss": 3,
            "vs_west_win": 5,
            "vs_west_loss": 1,
            "vs_east_win": 24,
            "vs_east_loss": 10,
            "vs_central_win": 17,
            "vs_central_loss": 5,
            "vs_interleague_win": 3,
            "vs_interleague_loss": 0,
            "vs_L_win": 15,
            "vs_L_loss": 5,
            "vs_R_win": 34,
            "vs_R_loss": 11,
        }
        team = Teams(**self.team_data)
        standing = Standings(**self.standing_data)
        db.create_all()
        db.session.add(team)
        db.session.add(standing)
        db.session.commit()

    def tearDown(self) -> None:
        if self.app_context:
            self.app_context.pop()
        db.session.remove()
        db.drop_all()

    def test_teams_page_render(self):
        response = self.client.get(url_for("teams.teams_page"))
        self.assertEqual(response.status_code, 200)
