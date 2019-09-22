class Volume:
    def __init__(self, volume, volume_air_ratio, surfaces, temperature):
        self.volume = volume
        self.volume_air_ratio = volume_air_ratio
        self.surfaces = surfaces
        self.temperature = temperature

    def air(self):
        return self.volume * self.volume_air_ratio

    def surface_loss(self, temperature_outside):
        return sum(s.surface_loss(self.temperature, temperature_outside) for s in self.surfaces)

    def solar_gain(self):
        return sum(s.solar_gain() for s in self.surfaces)

    def ventilation_loss(self, ventilation):
        return ventilation.loss(self.air(), self.temperature)