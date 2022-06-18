from . import r


def get_record(date, team, attr):
    return r.get_record(date, team, attr)


def set_record(date, team, values):
    r.set_record(date, team, values)
