import json
import redis


class Redis:
    def __init__(self, app=None):
        if app:
            self.host = app.config["REDIS_HOST"]
            self.port = app.config["REDIS_PORT"]
            self.password = app.config["REDIS_PASSWORD"]
            if self.password:
                self.redis = redis.Redis(
                    host=self.host, port=self.port, db=0, password=self.password
                )
            else:
                self.redis = redis.Redis(host=self.host, port=self.port, db=0)

    def init_app(self, app):
        self.host = app.config["REDIS_HOST"]
        self.port = app.config["REDIS_PORT"]
        self.password = app.config["REDIS_PASSWORD"]
        if self.password:
            self.redis = redis.Redis(
                host=self.host, port=self.port, db=0, password=self.password
            )
        else:
            self.redis = redis.Redis(host=self.host, port=self.port, db=0)

    def set_record(self, date, team, values):
        """store cache in redis

        Args:
            date (str): date
            team (str): team
            values (dict): dict with `attr: value` pairs
        """
        self.redis.hset(date, team, json.dumps(values))
        self.redis.expire(date, 60 * 60 * 24)

    def get_record(self, date, team, attr):
        """get cache from redis

        Args:
            date (str): date
            team (str): team
            attr (str): attr
        """
        res = self.redis.hget(date, team)
        if res:
            return json.loads(res)[attr]
        return None


r = Redis()
