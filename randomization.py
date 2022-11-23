import random

from solids import Ball, Cube, Ellipsoid, RectangularCuboid


def get_random_number(random_seed):
    random.seed(random_seed)
    # semi_axis_1 = random.randint(100)
    # semi_axis_2 = random.randint(100)
    # semi_axis_3 = random.randint(100)
    # length = random.randint(100)
    # width = random.randint(100)
    # height = random.randint(100)
    # radius = random.choice([semi_axis_1, semi_axis_2, semi_axis_3])
    # cube_side = random.choice([length, width, height])
    return random.randint(100)


