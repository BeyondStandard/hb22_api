import random


def get_car_type() -> str:
    return random.choice(["electric", "gasoline", "diesel"])
