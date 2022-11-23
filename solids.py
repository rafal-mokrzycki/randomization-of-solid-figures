import math


class Ellipsoid:
    """A class of Python object that describes the properties of an Ellipsoid"""

    def __init__(
        self,
        semi_axis_1,
        semi_axis_2,
        semi_axis_3,
    ):
        self.semi_axis_1 = semi_axis_1
        self.semi_axis_2 = semi_axis_2
        self.semi_axis_3 = semi_axis_3

    def compute_volume(self):
        return (4 / 3) * math.pi * self.semi_axis_1 * self.semi_axis_2 * self.semi_axis_3


class Ball(Ellipsoid):
    """A class of Python object that describes the properties of a Ball"""

    def __init__(self, radius):
        super().__init__(radius, radius, radius)


class RectangularCuboid:
    """A class of Python object that describes the properties of a Rectangular Cuboid"""

    def __init__(
        self,
        length,
        width,
        height,
    ):
        self.width = width
        self.height = height
        self.length = length

    def compute_volume(self):
        return self.width * self.height * self.length


class Cube(RectangularCuboid):
    """A class of Python object that describes the properties of a Cube"""

    def __init__(self, width):
        super().__init__(width, width, width)
