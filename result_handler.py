class ResultHandler:
    def __init__(self, db_client):
        self.db_client = db_client

    def handle(self, message):
        data = []
        data.append("{measurement},device={device} value={value} {timestamp}"
            .format(measurement=message['IEC61850'],
                    device=message['Device'],
                    value=message['Value'],
                    timestamp=message['Timestamp']))
        self.db_client.write_value(data)
