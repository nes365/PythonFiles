import math


def volume(r):
    """Returns the volume of a sphere with radius r"""
    if type(r) not in [int, float]:
        raise TypeError("The radius needs to be number")
    if r < 0:
        raise ValueError("The radius needs to be a positive integer")
    v = (4.0/3.0) * math.pi * r**3
    return v


print(volume(0))
