import json
from datetime import time

import requests


class HttpClient():

    def __init__(self, host, result_handler):
        self.host = host
        self.result_handler = result_handler

    async def receiveMessage(self):
        resp = requests.get(self.host)
        self.result_handler.handle(resp.json())
