class Surface:
    def __init__(self, area, u, u_correction, temperature_conditioned, windows):
        self.area = area
        self.u = u
        self.u_correction = u_correction  # e.g. decrease u for cellar floor because earth isolates better than air
        self.temperature_conditioned = temperature_conditioned
        self.windows = windows

    @property
    def area_without_windows(self):
        return self.area - sum(w.area for w in self.windows)

    def surface_loss(self, temperature_insided, temperature_outside):
        t = self.temperature_conditioned if self.temperature_conditioned is not None else temperature_outside
        temperature_delta = temperature_insided - t
        return self.area_without_windows * self.u * self.u_correction * temperature_delta + \
            sum(w.surface_loss(temperature_delta) for w in self.windows)

    def solar_gain(self):
        return sum(w.solar_gain() for w in self.windows)

