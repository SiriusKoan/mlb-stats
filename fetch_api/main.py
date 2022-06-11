from os import getenv
from datetime import datetime
import requests


class Updater:
    def __init__(self, start_year=datetime.today().strftime("%Y")) -> None:
        self.db_uri = getenv("DB_URI")
        self.start_year = start_year
        self.standing_url = "https://statsapi.mlb.com/api/v1/standings?leagueId=103,104&season={season}&date={date}&standingsTypes=regularSeason&hydrate=division,conference,league,team"
        self.season_info_url = "https://statsapi.mlb.com/api/v1/seasons/all/?sportId=1"

    def get_all_season_info(self):
        """Return a list containing all season info

        Returns:
            list: A list containing all season info
        """
        r = requests.get(self.season_info_url)
        return r.json()["seasons"]

    def get_all(self):
        pass

    def get_by_date(self, date=datetime.today().strftime("%Y-%m-%d")):
        year = date.split("-")[0]
        res = requests.get(self.standing_url.format(season=year, date=date)).json()
        teams = []
        for div in res["records"]:
            for team in div["teamRecords"]:
                teamname = team["team"]["teamName"]
                league = team["team"]["league"]["id"]
                wins = team["wins"]
                losses = team["losses"]
                GB = team["gamesBack"] if team["gamesBack"] != "-" else 0
                WCGB = (
                    team["wildCardGamesBack"] if team["wildCardGamesBack"] != "-" else 0
                )
                RA = team["runsAllowed"]
                RS = team["runsScored"]
                split_records = team["records"]["splitRecords"]
                home_win = split_records[0]["wins"]
                home_loss = split_records[0]["losses"]
                away_win = split_records[1]["wins"]
                away_loss = split_records[1]["losses"]
                vs_L_win = split_records[2]["wins"]
                vs_L_loss = split_records[2]["losses"]
                vs_R_win = split_records[7]["wins"]
                vs_R_loss = split_records[7]["losses"]
                XTRA_win = split_records[9]["wins"]
                XTRA_loss = split_records[9]["losses"]
                one_run_win = split_records[10]["wins"]
                one_run_loss = split_records[10]["losses"]
                vs_500_win = split_records[11]["wins"]
                vs_500_loss = split_records[11]["losses"]
                day_game_win = split_records[12]["wins"]
                day_game_loss = split_records[12]["losses"]
                night_game_win = split_records[13]["wins"]
                night_game_loss = split_records[13]["losses"]
                grass_game_win = split_records[14]["wins"]
                grass_game_loss = split_records[14]["losses"]
                turf_game_win = split_records[15]["wins"]
                turf_game_loss = split_records[15]["losses"]
                division_records = team["records"]["divisionRecords"]
                vs_west_win = division_records[0]["wins"]
                vs_west_loss = division_records[0]["losses"]
                vs_east_win = division_records[1]["wins"]
                vs_east_loss = division_records[1]["losses"]
                vs_central_win = division_records[2]["wins"]
                vs_central_loss = division_records[2]["losses"]
                league_records = team["records"]["leagueRecords"]
                if league == 103:
                    vs_interleague_win = league_records[1]["wins"]
                    vs_interleague_loss = league_records[1]["losses"]
                else:
                    vs_interleague_win = league_records[0]["wins"]
                    vs_interleague_loss = league_records[0]["losses"]
                teams.append(
                    {
                        "teamname": teamname,
                        "wins": wins,
                        "losses": losses,
                        "GB": GB,
                        "WCGB": WCGB,
                        "XTRA_win": XTRA_win,
                        "XTRA_loss": XTRA_loss,
                        "RS": RS,
                        "RA": RA,
                        "home_win": home_win,
                        "home_loss": home_loss,
                        "away_win": away_win,
                        "away_loss": away_loss,
                        "vs_500_win": vs_500_win,
                        "vs_500_loss": vs_500_loss,
                        "one_run_win": one_run_win,
                        "one_run_loss": one_run_loss,
                        "day_game_win": day_game_win,
                        "day_game_loss": day_game_loss,
                        "night_game_win": night_game_win,
                        "night_game_loss": night_game_loss,
                        "grass_game_win": grass_game_win,
                        "grass_game_loss": grass_game_loss,
                        "turf_game_win": turf_game_win,
                        "turf_game_loss": turf_game_loss,
                        "vs_west_win": vs_west_win,
                        "vs_west_loss": vs_west_loss,
                        "vs_east_win": vs_east_win,
                        "vs_east_loss": vs_east_loss,
                        "vs_central_win": vs_central_win,
                        "vs_central_loss": vs_central_loss,
                        "vs_interleague_win": vs_interleague_win,
                        "vs_interleague_loss": vs_interleague_loss,
                        "vs_L_wins": vs_L_win,
                        "vs_L_loss": vs_L_loss,
                        "vs_R_wins": vs_R_win,
                        "vs_R_loss": vs_R_loss,
                    }
                )
        return teams
