#!/usr/bin/python
from threading import Thread
from time import sleep

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

from exporter import Exporter
from kwhMeter import KwhMeter

devices = []

app = Flask(__name__)
metrics = PrometheusMetrics(app)
exporter = Exporter()


def init():
    ids = [1]
    master_serial_device = '/dev/tty.usbserial-1420'
    print('Adding {} Devices on {}'.format(len(devices), master_serial_device))
    for device in ids:
        devices.append(KwhMeter(device, master_serial_device))


def read_values():
    print('Reading devices')
    for rs485 in devices:
        measurement = rs485.query()
        exporter.register(rs485.id, measurement)


def refresh_values():
    while True:
        read_values()
        sleep(3)


if __name__ == '__main__':
    init()
    Thread(target=refresh_values).start()
    app.run()
