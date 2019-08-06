from math import pi
import logging

# Create and configure logger
logging.basicConfig(filename="./circleArea.log",
                    level=logging.DEBUG)
logger = logging.getLogger()

# Test logger
logger.info("Test log message")

def circle_area(r):
    """This function takes radius r as an input and calculates the area of a circle."""
    if  type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError("You can't calculate the area of a circle when the radius is a negative number.")
    
    return pi*(r**2)



