import minimalmodbus

from measurements import read_modbus_device

BAUDRATE = 9600


class KwhMeter:
    rs485 = None
    id = None

    volts_guage = None

    def __init__(self, device_id, master_serial_device):
        self.id = device_id
        self.rs485 = minimalmodbus.Instrument(master_serial_device, device_id)
        self.rs485.serial.baudrate = BAUDRATE
        self.rs485.serial.bytesize = 8
        self.rs485.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.rs485.serial.stopbits = 1
        self.rs485.serial.timeout = 1
        self.rs485.debug = False
        self.rs485.mode = minimalmodbus.MODE_RTU

    def query(self):
        return read_modbus_device(self)
