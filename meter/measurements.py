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



