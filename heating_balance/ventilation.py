from .units import *

class Ventilation:
    def __init__(self, change_rate, temperature_outside, efficiency):
        self.density_air = 1.2041 * kg / m3  # at 20 degree celsius
        self.specific_heat_capacity_air = 1005.0 * J / (kg * K)  # isobar, standard conditions
        self.change_rate = change_rate
        self.temperature_outside = temperature_outside
        self.efficiency = efficiency

    def loss(self, volume, temperature_inside):
        air_mass = self.density_air * volume * (1.0 - self.efficiency)
        temperature_delta = temperature_inside - self.temperature_outside
        return (air_mass * self.change_rate * self.specific_heat_capacity_air * temperature_delta).to(W)
