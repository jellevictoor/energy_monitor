from prometheus_client import Gauge


class Exporter:

    def __init__(self):
        self.volt_gauge = Gauge("voltage", "the voltage in volts", ['device_id'])
        self.current_gauge = Gauge("current", "The current in amps", ['device_id'])
        self.active_power_gauge = Gauge("active_power", "The active power in watts", ['device_id'])
        self.apparent_power_gauge = Gauge("apparent_power", "The apparent power in VoltAmps", ['device_id'])
        self.reactive_power_gauge = Gauge("reactive_power", "The reactive power in VAr", ['device_id'])
        self.power_factor_gauge = Gauge("power_factor", "The power factor (should be 1)", ['device_id'])
        self.phase_angle_gauge = Gauge("phase_angle", "The phase angle in Degrees", ['device_id'])
        self.frequency_gauge = Gauge("frequency", "The frequency in Hz", ['device_id'])
        self.import_gauge = Gauge("import_active_energy", "The import active engery in Kwh", ['device_id'])
        self.export_gauge = Gauge("export_active_energy", "The export active engery in Kwh", ['device_id'])
        self.import_reactive_gauge = Gauge("import_reactive_energy", "The import reactive engery in kvarh", ['device_id'])
        self.export_reactive_gauge = Gauge("export_reactive_energy", "The export reactive engery in kvarh", ['device_id'])
        self.total_active_energy_gauge = Gauge("total_active_energy", "The total active energy in kwh", ['device_id'])
        self.total_reactive_energy_gauge = Gauge("total_reactive_energy", "The total active energy in kwh", ['device_id'])

    def register(self, device_id, measurement):
        self.register_value(device_id, self.volt_gauge, measurement.volts)
        self.register_value(device_id, self.current_gauge, measurement.current)
        self.register_value(device_id, self.active_power_gauge, measurement.active_power)
        self.register_value(device_id, self.reactive_power_gauge, measurement.reactive_power)
        self.register_value(device_id, self.power_factor_gauge, measurement.power_factor)
        self.register_value(device_id, self.phase_angle_gauge, measurement.phase_angle)
        self.register_value(device_id, self.frequency_gauge, measurement.frequency)
        self.register_value(device_id, self.import_gauge, measurement.import_active_energy)
        self.register_value(device_id, self.export_gauge, measurement.export_active_energy)
        self.register_value(device_id, self.import_reactive_gauge, measurement.import_reactive_energy)
        self.register_value(device_id, self.export_reactive_gauge, measurement.export_reactive_energy)
        self.register_value(device_id, self.total_active_energy_gauge, measurement.total_active_energy)
        self.register_value(device_id, self.total_reactive_energy_gauge, measurement.total_reactive_energy)

    def register_value(self, device_id, gauge, value):
        if value != -1:
            gauge.labels(device_id).set(value)
