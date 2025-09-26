# my_geometry_package/shapes.py

import math

def circle_area(radius):
    """Calculates the area of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

def square_area(side):
    """Calculates the area of a square."""
    if side < 0:
        raise ValueError("Side length cannot be negative.")
    return side ** 2