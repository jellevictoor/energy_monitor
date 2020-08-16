from influxdb import InfluxDBClient


class InfluxClient:
    def __init__(self,host, port, db):
        self.client = InfluxDBClient(host, port, db)
        self.db = db

    def write_value(self, body):
        self.client.write_points(body,database=self.db, time_precision='ms', batch_size=10000, protocol='line')
