from dataclasses import dataclass




@dataclass
class Measurement:
    volts: float = None
    current: float = None
    active_power: float = None
    apparent_power: float = None
    reactive_power: float = None
    power_factor: float = None
    phase_angle: float = None
    frequency: float = None
    import_active_energy: float = None
    export_active_energy: float = None
    import_reactive_energy: float = None
    export_reactive_energy: float = None
    total_active_energy: float = None
    total_reactive_energy: float = None

    def print(self):
        print('Voltage: {0:.1f} Volts'.format(self.volts))
        print('Current: {0:.1f} Amps'.format(self.current))
        print('Active power: {0:.1f} Watts'.format(self.active_power))
        print('Apparent power: {0:.1f} VoltAmps'.format(self.apparent_power))
        print('Reactive power: {0:.1f} VAr'.format(self.reactive_power))
        print('Power factor: {0:.1f}'.format(self.power_factor))
        print('Phase angle: {0:.1f} Degree'.format(self.phase_angle))
        print('Frequency: {0:.1f} Hz'.format(self.frequency))
        print('Import active energy: {0:.3f} Kwh'.format(self.import_active_energy))
        print('Export active energy: {0:.3f} kwh'.format(self.export_active_energy))
        print('Import reactive energy: {0:.3f} kvarh'.format(self.import_reactive_energy))
        print('Export reactive energy: {0:.3f} kvarh'.format(self.export_reactive_energy))
        print('Total active energy: {0:.3f} kwh'.format(self.total_active_energy))
        print('Total reactive energy: {0:.3f} kvarh'.format(self.total_reactive_energy))
        print('Current Yield (V*A): {0:.1f} Watt'.format(self.volts * self.current))

def read_modbus_device(device):
    measurement = Measurement()
    modbus_device = device.rs485
    measurement.volts = try_read(modbus_device, 0, 4, 2)
    measurement.current = try_read(modbus_device, 6, 4, 2)
    measurement.active_power = try_read(modbus_device, 12, 4, 2)
    measurement.apparent_power = try_read(modbus_device, 18, 4, 2)
    measurement.reactive_power = try_read(modbus_device, 24, 4, 2)
    measurement.power_factor = try_read(modbus_device, 30, 4, 2)
    measurement.phase_angle = try_read(modbus_device, 36, 4, 2)
    measurement.frequency = try_read(modbus_device, 70, 4, 2)
    measurement.import_active_energy = try_read(modbus_device, 72, 4, 2)
    measurement.export_active_energy = try_read(modbus_device, 74, 4, 2)
    measurement.import_reactive_energy = try_read(modbus_device, 76, 4, 2)
    measurement.export_reactive_energy = try_read(modbus_device, 78, 4, 2)
    measurement.total_active_energy = try_read(modbus_device, 342, 4, 2)
    measurement.total_reactive_energy = try_read(modbus_device, 344, 4, 2)
    return measurement

def try_read(modbus_device, registeraddress, function_code, number_of_registers):
    try:
        return modbus_device.read_float(registeraddress, functioncode=function_code, number_of_registers=number_of_registers)
    except:
        print("Could not read")
        return -1

