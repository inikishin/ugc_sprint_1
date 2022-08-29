import backoff
from clickhouse_driver import Client
from clickhouse_driver.errors import NetworkError

from backoff_hdlr import backoff_hdlr


class Load:
    @backoff.on_exception(backoff.expo,
                          NetworkError,
                          on_backoff=backoff_hdlr)
    def __init__(self, host):
        self.client = Client(host=host)

    @backoff.on_exception(backoff.expo,
                          NetworkError,
                          on_backoff=backoff_hdlr)
    def _execute(self, query: str, data: list) -> int:
        return self.client.execute(query, data)

    def insert_bookmark_data(self, data: list) -> None:
        self._execute(
            "INSERT INTO bookmarks (movie_id, user_id) VALUES",
            data)

    def insert_rating_data(self, data: list) -> None:
        self._execute(
            "INSERT INTO ratings (movie_id, user_id, rating) VALUES",
            data)

    def insert_history_data(self, data: list) -> None:
        self._execute(
            "INSERT INTO history (movie_id, user_id, viewed) VALUES",
            data)

    def insert_last_view_time_data(self, data: list) -> None:
        self._execute(
            "INSERT INTO last_view_time (movie_id, user_id, paused_sec) VALUES",
            data)
