import random

from solids import Ball, Cube, Ellipsoid, RectangularCuboid


def get_class_name_of_max_value(random_seed, length=20):
    """Returns class name with the greatest volume."""
    random.seed(random_seed)
    seq = random.sample(range(1, 100), length)
    ball = Ball(random.choice(seq))
    cube = Cube(random.choice(seq))
    ellipsoid = Ellipsoid(random.choice(seq), random.choice(seq), random.choice(seq))
    rect_cube = RectangularCuboid(
        random.choice(seq), random.choice(seq), random.choice(seq)
    )
    lst = []
    for obj in [ball, cube, ellipsoid, rect_cube]:
        lst.append((obj.__class__.__name__, obj.compute_volume()))

    return max(lst, key=lambda item: item[1])
