import backoff
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

from backoff_hdlr import backoff_hdlr
from constants import TOPIC_BOOKMARKS, TOPIC_RATING, TOPIC_VIEWS, TOPIC_LAST_VIEW


class Extract:
    @backoff.on_exception(backoff.expo,
                          [NoBrokersAvailable, ValueError],
                          on_backoff=backoff_hdlr)
    def __init__(self, transform, load, host):
        self.extract = KafkaConsumer(
            TOPIC_BOOKMARKS, TOPIC_RATING, TOPIC_VIEWS, TOPIC_LAST_VIEW,
            bootstrap_servers=[host],
            auto_offset_reset='earliest',
            group_id='etl-clickhouse',
        )
        self.transform = transform
        self.load = load

    @backoff.on_exception(backoff.expo,
                          [NoBrokersAvailable, ValueError],
                          on_backoff=backoff_hdlr)
    def run(self):
        for message in self.extract:
            if message.topic == TOPIC_BOOKMARKS:
                data = self.transform.get_bookmark_data(message.key.decode('utf-8'),
                                                        message.value.decode('utf-8'))
                print(data)
                self.load.insert_bookmark_data([data])
            elif message.topic == TOPIC_RATING:
                data = self.transform.get_rating_data(message.key.decode('utf-8'),
                                                      message.value.decode('utf-8'))
                print(data)
                self.load.insert_rating_data([data])
            elif message.topic == TOPIC_VIEWS:
                data = self.transform.get_history_data(message.key.decode('utf-8'),
                                                       message.value.decode('utf-8'))
                print(data)
                self.load.insert_history_data([data])
            elif message.topic == TOPIC_LAST_VIEW:
                data = self.transform.get_last_view_time_data(message.key.decode('utf-8'),
                                                              message.value.decode('utf-8'))
                print(data)
                self.load.insert_last_view_time_data([data])
            else:
                print(f'Unknown topic: {message.topic}')
                print('Message:')
                print('key', message.key.decode('utf-8'))
                print('value', message.value.decode('utf-8'))
