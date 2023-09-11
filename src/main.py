import numpy as np

from randomization import get_class_name_of_max_value


def main():
    """Returns info about the figure that has the greatest volume
    for a random seed given by the user."""
    while True:
        random_seed = input("Type in a number (`q` to quit): ")
        if random_seed == "q":
            print("Program finished")
            break
        result = get_class_name_of_max_value(random_seed)
        print(
            f"For the random seed={random_seed} '{result[0]}' \
has the greates volume of {np.round(float(result[1]),2)} units."
        )


if __name__ == "__main__":
    main()
