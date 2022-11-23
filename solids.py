import math


class Ellipsoid:
    """A class of Python object that describes the properties of an Ellipsoid"""

    def __init__(
        self,
        semi_axis_1,
        semi_axis_2,
        semi_axis_3,
        # focus_1,
        # focus_2,
        # focus_3,
        center=(0, 0, 0),
    ):
        self.semi_axis_1 = semi_axis_1
        self.semi_axis_2 = semi_axis_2
        self.semi_axis_3 = semi_axis_3
        self.focus_1 = "focus_1"
        self.focus_2 = "focus_2"
        self.focus_3 = "focus_3"
        self.center = center

    def __repr__(self):
        return f"""
Ellipsoid(a={self.semi_axis_1}, b={self.semi_axis_2}, c={self.semi_axis_3}
focuses=({self.focus_1}, {self.focus_2}, {self.focus_3}) center={self.center})"""

    def compute_volume(self):
        return (4 / 3) * math.pi * self.semi_axis_1 * self.semi_axis_2 * self.semi_axis_3


class Ball(Ellipsoid):
    def __init__(self, radius, center=(0, 0, 0)):
        super().__init__(radius, radius, radius, center)
