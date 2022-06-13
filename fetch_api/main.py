from datetime import datetime, timedelta
import requests
from db_helper import create_all, insert_to_teams, insert_to_standings


class Updater:
    def __init__(self, start_year=int(datetime.today().strftime("%Y"))) -> None:
        self.start_year = start_year
        self.this_year = int(datetime.today().strftime("%Y"))
        self.standing_url = "https://statsapi.mlb.com/api/v1/standings?leagueId=103,104&season={season}&date={date}&standingsTypes=regularSeason&hydrate=division,conference,league,team"
        self.season_info_url = "https://statsapi.mlb.com/api/v1/seasons/all/?sportId=1"
        self.team_info_url = (
            "https://statsapi.mlb.com/api/v1/teams?sportId=1&leagueIds=103,104"
        )

    def insert_to_db(self):
        """Insert all data to database"""
        print("Creating database...")
        create_all()
        print("Inserting teams...")
        insert_to_teams(self.get_all_teams_info())
        print("Inserting standings...")
        for standing in self.get_all():
            insert_to_standings(standing)

    def get_all_teams_info(self):
        """Return a list containing all teams info

        Returns:
            list: A list containing all teams info
        """
        r = requests.get(self.team_info_url)
        return r.json()["teams"]

    def get_all_season_info(self):
        """Return a list containing all season info

        Returns:
            list: A list containing all season info
        """
        r = requests.get(self.season_info_url)
        return r.json()["seasons"]

    def days_between(self, start_day, end_day):
        """Yield next day in the range of start_day and end_day"""
        start_day = datetime.strptime(start_day, "%Y-%m-%d")
        end_day = datetime.strptime(end_day, "%Y-%m-%d")
        while start_day <= end_day:
            yield start_day.strftime("%Y-%m-%d")
            start_day += timedelta(days=1)

    def get_all(self):
        """Get all standings for specified season (year) range

        Returns:
            list: A list containing all standings during the specified season range
        """
        season_info = self.get_all_season_info()
        # 1876 is the starting year in API
        for i in range(self.start_year - 1876, self.this_year + 1 - 1876):
            data = []
            print("Starting to fetch standings for season {}".format(i))
            start_day = season_info[i]["regularSeasonStartDate"]
            end_day = season_info[i]["regularSeasonEndDate"]
            for day in self.days_between(start_day, end_day):
                if day > datetime.today().strftime("%Y-%m-%d"):
                    break
                data.append(self.get_standing_by_date(day))
            yield data

    def get_standing_by_date(self, date=datetime.today().strftime("%Y-%m-%d")):
        """Get standings for a specific date

        Args:
            date (str): The date to get standings for

        Returns:
            list: A list containing all teams' standings on the specified date
        """
        year = date.split("-")[0]
        res = requests.get(self.standing_url.format(season=year, date=date)).json()
        teams = []
        for div in res["records"]:
            for team in div["teamRecords"]:
                team_id = team["team"]["id"]
                league = team["team"]["league"]["id"]
                wins = team["wins"]
                losses = team["losses"]
                division_rank = team["divisionRank"]
                league_rank = team["leagueRank"]
                GB = float(team["gamesBack"] if team["gamesBack"] != "-" else 0)
                tmp = (
                    team["wildCardGamesBack"] if team["wildCardGamesBack"] != "-" else 0
                )
                WCGB = -1 * float(tmp) if str(tmp).startswith("+") else float(tmp)
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
                if len(split_records) == 16:
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
                else:
                    # Sometimes there is not "winner" record, I think it's because no teams reach .500 in first few games
                    vs_500_win = 0
                    vs_500_loss = 0
                    day_game_win = split_records[11]["wins"]
                    day_game_loss = split_records[11]["losses"]
                    night_game_win = split_records[12]["wins"]
                    night_game_loss = split_records[12]["losses"]
                    grass_game_win = split_records[13]["wins"]
                    grass_game_loss = split_records[13]["losses"]
                    turf_game_win = split_records[14]["wins"]
                    turf_game_loss = split_records[14]["losses"]
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
                        "team_id": team_id,
                        "date": datetime.strptime(date, "%Y-%m-%d"),
                        # "date": date,
                        "win": wins,
                        "loss": losses,
                        "division_rank": division_rank,
                        "league_rank": league_rank,
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
