from .models import Teams, Standings


def get_all_teams():
    """
    Returns a list of all teams in the database.
    """
    return to_dict(Teams.query.all())


def get_all_standings():
    """
    Returns a list of all standings in the database.
    """
    return to_dict(Standings.query.all())


def get_standings_in_season(start_season, end_season=None, teams=[], attrs=[]):
    """
    Returns a list of standings in the database between the start and end
    indices.

    Args:
        start_season (int): The start season to get standings for.
        end_season (int): The end season to get standings for.
        teams (list): A list of teams to get.
        attrs (list): A list of attributes to get.

    Returns:
        list: A list of standings in the database between the start and end with specified teams and attributes.
    """
    start = start_season + "-01-01"
    end = (end_season if end_season else start_season) + "-12-31"
    Filter = Standings.query.filter(Standings.date.between(start, end))
    Filter = Filter.filter(Standings.team_id.in_(teams))
    return to_dict(Filter.all(), attrs=attrs)


def to_dict(data, attrs="all"):
    """
    Returns a list of dictionaries of the data.

    Args:
        data (list): A list of data to convert to dictionaries.
        attrs (list): A list of attributes to get.

    Returns:
        list: A list of dictionaries of the data.
    """
    if attrs == "all":
        return [
            {k: v for k, v in standing.__dict__.items() if k[0] != "_"}
            for standing in data
        ]
    else:
        return [{attr: getattr(standing, attr) for attr in attrs} for standing in data]
