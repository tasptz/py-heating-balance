class Window:
    def __init__(self, area, area_glass_ratio, u, g, solar_radiation):
        self.area = area
        self.area_glass_ratio = area_glass_ratio
        self.u = u
        self.g = g
        self.solar_radiation = solar_radiation

    def surface_loss(self, temperature_delta):
        return self.area * self.u * temperature_delta

    def solar_gain(self):
        return self.area * self.area_glass_ratio * self.g * self.solar_radiation