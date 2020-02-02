from math import pi
import logging

# Create and configure logger
LOG_FORMAT="%(levelname)s : %(asctime)s : %(message)s"
logging.basicConfig(filename="./circleArea.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

# Test logger
#logger.debug("Debug message")
#logger.info("Test log message")
#logger.warning("I'm warning you")
#logger.error("Nope")
#logger.critical("Melt down")


def circle_area(r):
    """This function takes radius r as an input and calculates the area of a circle."""
    if type(r) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r < 0:
        raise ValueError(
            "You can't calculate the area of a circle when the radius is a negative number.")

    return round(pi*(r**2), 2)


r = int(input("Enter radius in cm: "))
print("Circle area is: ", circle_area(r), "cm^2")
logger.info("Input value %s", r)
