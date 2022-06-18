from datetime import timedelta, datetime
from ..database import helper as db_helper
from ..redis import helper as redis_helper


def get_date_range(start_date, end_date):
    """
    Get a list of dates between start and end.
    """
    cur = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    while cur <= end:
        yield cur.strftime("%Y-%m-%d")
        cur += timedelta(days=1)


def get_standings_with_date_range(start_date, end_date, teams, attrs):
    """
    Get standings for a given date range and teams from redis or db.
    """
    return db_helper.get_standings_with_date_range(start_date, end_date, teams, attrs)
    # result = []
    # for team in teams:
    #     tmp = []
    #     for date in get_date_range(start_date, end_date):
    #         tmp_dict = dict()
    #         left_attrs = []
    #         for attr in attrs:
    #             res = redis_helper.get_record(date, team, attr)
    #             if res is None:
    #                 left_attrs.append(attr)
    #             else:
    #                 tmp_dict[attr] = res
    #                 # print(f"{attr} = {res} is from redis")
    #         if left_attrs:
    #             res = db_helper.get_standings_by_date(date, team, left_attrs)
    #             if res:
    #                 tmp_dict = {**tmp_dict, **res[0]}
    #                 del res[0]["date"]
    #                 redis_helper.set_record(date, team, res[0])
    #                 # print(f"{res} is from db")
    #         tmp_dict["date"] = date
    #         tmp.append(tmp_dict)
    #     result.append(tmp)
    # return result


def get_all_teams():
    """
    Get all teams from redis or db.
    """
    return db_helper.get_all_teams()
