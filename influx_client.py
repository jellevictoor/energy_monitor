import time

from influxdb import InfluxDBClient


class InfluxClient:
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db
        self.client = None
        self.connect()

    def connect(self):
        self.client = InfluxDBClient(self.host, self.port, self.db)

    def write_value(self, body):
        try:
            self.client.write_points(body, database=self.db, time_precision='ms', batch_size=10000, protocol='line')
        except Exception as e:
            print('Connection with server closed, reconnecting')
            self.client.close()
            time.sleep(2)
            self.connect()
