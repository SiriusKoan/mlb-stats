from .models import Teams, Standings


def get_all_teams():
    """
    Returns a list of all teams in the database.
    """
    return to_dict(Teams.query.order_by(Teams.league).order_by(Teams.division).all())


def get_all_standings():
    """
    Returns a list of all standings in the database.
    """
    return to_dict(Standings.query.all())


def get_standing_attrs():
    """
    Returns a list of all attributes in the standings table.
    """
    return [attr for attr in Standings.__table__.columns.keys() if attr[0] != "_"]


def get_standings_with_date_range(start_date, end_date=None, teams=[], attrs=[]):
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
    if (end_date is None):
        end_date = start_date
    Filter = Standings.query.filter(Standings.date.between(start_date, end_date))
    result = []
    for team in teams:
        tmp = Filter.filter_by(team_id=team)
        result.append(to_dict(tmp.all(), attrs=attrs))
    return result


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
        if "date" not in attrs:
            attrs.append("date")
        return [{attr: getattr(standing, attr) for attr in attrs} for standing in data]
