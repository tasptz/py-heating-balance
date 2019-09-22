class Window:
    def __init__(self, area, glass_area_ratio, u, g, solar_radiation):
        self.area = area
        self.glass_area_ratio = glass_area_ratio
        self.u = u
        self.g = g
        self.solar_radiation = solar_radiation

    def surface_loss(self, temperature_delta):
        return self.area * self.u * temperature_delta

    def solar_gain(self):
        return self.area * self.glass_area_ratio * self.g * self.solar_radiation