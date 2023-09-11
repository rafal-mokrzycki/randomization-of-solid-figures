import math


class Ellipsoid:
    """A class used to represent an Ellipsoid

    Attributes
    ----------
    semi_axis_1 : int | float
        semi axis (a)

    semi_axis_2 : int | float
        semi axis (b)

    semi_axis_3 : int | float
        semi axis (c)


    Methods
    ----------
    compute_volume()
        Returns Ellipsoid's volume
    """

    def __init__(
        self,
        semi_axis_1: int | float,
        semi_axis_2: int | float,
        semi_axis_3: int | float,
    ):
        self.semi_axis_1 = semi_axis_1
        self.semi_axis_2 = semi_axis_2
        self.semi_axis_3 = semi_axis_3

    def compute_volume(self):
        """Return Ellipsoid's volume (without any unit)."""

        return (4 / 3) * math.pi * self.semi_axis_1 * self.semi_axis_2 * self.semi_axis_3


class Ball(Ellipsoid):
    """A class used to represent a Ball (inherits from Ellipsoid)

    Attributes
    ----------
    radius : int | float
        radius (R)
    """

    def __init__(self, radius: int | float):
        super().__init__(radius, radius, radius)


class RectangularCuboid:
    """A class used to represent a Rectangular Cuboid

    Attributes
    ----------

    length : int | float
        length (a)

    width : int | float
        width (b)

    height : int | float
        height (h)


    Methods
    ----------
    compute_volume()
        Returns Rectangular Cuboid's volume
    """

    def __init__(
        self,
        length: int | float,
        width: int | float,
        height: int | float,
    ):
        self.width = width
        self.height = height
        self.length = length

    def compute_volume(self):
        """Return Rectangular Cuboid's volume (without any unit)."""

        return self.width * self.height * self.length


class Cube(RectangularCuboid):
    """A class used to represent a Cube (inherits from Rectangular Cuboid)

    Attributes
    ----------

    width : int | float
        width (b)"""

    def __init__(self, width: int | float):
        super().__init__(width, width, width)


class Cone:
    """A class used to represent a Cone

    Attributes
    ----------
    radius : int | float
        base radius (R)

    height : int | float
        height (H)

    parameter : int | float
        used to generalize the volume equation for inheriting classes (figures)


    Methods
    ----------
    compute_volume()
        Returns Cone's volume
    """

    def __init__(
        self, radius: int | float, height: int | float, parameter: int | float = 3
    ):
        self.radius = radius
        self.height = height
        self.parameter = parameter

    def compute_volume(self):
        """Return Cone's volume (without any unit)."""

        return (1 / self.parameter) * math.pi * (self.radius**2) * self.height


class Cylinder(Cone):
    """A class used to represent a Cylinder (inherits from Cone)

    Attributes
    ----------

    radius : int | float
        base radius (R)

    height : int | float
        height (H)

    parameter : int | float
        used to compute a proper volume"""

    def __init__(
        self, radius: int | float, height: int | float, parameter: int | float = 1
    ):
        super().__init__(radius, height, parameter)
