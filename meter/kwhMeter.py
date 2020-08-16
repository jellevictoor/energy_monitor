import minimalmodbus

from measurements import Measurement

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
        measurement = Measurement()
        modbus_device = self.rs485
        measurement.volts = self.try_read(modbus_device, 0, 4, 2)
        measurement.current = self.try_read(modbus_device, 6, 4, 2)
        measurement.active_power = self.try_read(modbus_device, 12, 4, 2)
        measurement.apparent_power = self.try_read(modbus_device, 18, 4, 2)
        measurement.reactive_power = self.try_read(modbus_device, 24, 4, 2)
        measurement.power_factor = self.try_read(modbus_device, 30, 4, 2)
        measurement.phase_angle = self.try_read(modbus_device, 36, 4, 2)
        measurement.frequency = self.try_read(modbus_device, 70, 4, 2)
        measurement.import_active_energy = self.try_read(modbus_device, 72, 4, 2)
        measurement.export_active_energy = self.try_read(modbus_device, 74, 4, 2)
        measurement.import_reactive_energy = self.try_read(modbus_device, 76, 4, 2)
        measurement.export_reactive_energy = self.try_read(modbus_device, 78, 4, 2)
        measurement.total_active_energy = self.try_read(modbus_device, 342, 4, 2)
        measurement.total_reactive_energy = self.try_read(modbus_device, 344, 4, 2)
        return measurement

    def try_read(modbus_device, registeraddress, function_code, number_of_registers):
        try:
            return modbus_device.read_float(registeraddress, functioncode=function_code, number_of_registers=number_of_registers)
        except:
            print("Could not read")
            return -1
