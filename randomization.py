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
    return random.randint(1, 100)


def interact_with_computer():
    random_seed = input("Type in a number: ")
    ball = Ball(get_random_number(random_seed))
    cube = Cube(get_random_number(random_seed))
    ellipsoid = Ellipsoid(
        get_random_number(random_seed),
        get_random_number(random_seed),
        get_random_number(random_seed),
    )
    rect_cube = RectangularCuboid(
        get_random_number(random_seed),
        get_random_number(random_seed),
        get_random_number(random_seed),
    )
    return get_class_name_of_max_value(
        ball.compute_volume(),
        cube.compute_volume(),
        ellipsoid.compute_volume(),
        rect_cube.compute_volume(),
    )


def get_class_name_of_max_value(*args):
    return max(*args)
