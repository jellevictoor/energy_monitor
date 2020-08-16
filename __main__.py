import asyncio

from influx_client import InfluxClient
from result_handler import ResultHandler
from websocket_client import WebSocketClient

if __name__ == '__main__':
    db_client = InfluxClient('192.168.1.4', 8086, 'energy')
    handler = ResultHandler(db_client)

    client = WebSocketClient('ws://192.168.1.4:8080/ws', handler)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())
    # Start listener and heartbeat
    tasks = [
        asyncio.ensure_future(client.receiveMessage()),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
