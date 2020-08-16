import asyncio
import json
import time

import websockets


class WebSocketClient():

    def __init__(self, host, result_handler):
        self.host = host
        self.result_handler = result_handler

    async def connect(self):
        '''
            Connecting to webSocket server

            websockets.client.connect returns a WebSocketClientProtocol, which is used to send and receive messages
        '''
        self.connection = await websockets.client.connect(self.host)
        if self.connection.open:
            print('Connection stablished. Client correcly connected')

    async def receiveMessage(self):
        while True:
            try:
                message = await self.connection.recv()
                dict = json.loads(message)
                if 'Device' in dict:
                    print('writing: {}'.format(message))
                    self.result_handler.handle(dict)
                else:
                    print('ignoring: {}'.format(message))
            except websockets.exceptions.ConnectionClosed as e:
                print('Connection with server closed, reconnecting')
                time.sleep(2)
                await self.connect()

    async def heartbeat(self, connection):
        '''
        Sending heartbeat to server every 5 seconds
        Ping - pong messages to verify connection is alive
        '''
        while True:
            try:
                await connection.send('ping')
                await asyncio.sleep(5)
            except websockets.exceptions.ConnectionClosed:
                print('Connection with server closed')
                break
