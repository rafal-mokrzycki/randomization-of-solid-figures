""" to run: python -m pytest -vv test_solids.py -s
add --pdb to debug in command line
use VScode test tools reccomended (the beaker)
to debug VScode: pytest --collect-only """

from solids import Ball, Cone, Cube, Cylinder, Ellipsoid, RectangularCuboid


def test_compute_volume_ball():
    b = Ball(1)
    assert b.compute_volume() == 4.1887902047863905


def test_compute_volume_ellipsoid():
    e = Ellipsoid(1, 1, 1)
    assert e.compute_volume() == 4.1887902047863905


def test_compute_volume_rect_cuboid():
    r = RectangularCuboid(1, 2, 3)
    assert r.compute_volume() == 6


def test_compute_volume_cube():
    cube = Cube(3)
    assert cube.compute_volume() == 27


def test_compute_volume_cone():
    cone = Cone(1, 3)
    assert cone.compute_volume() == 3.141592653589793


def test_compute_volume_cylinder():
    cylinder = Cylinder(1, 3)
    assert cylinder.compute_volume() == 9.42477796076938
