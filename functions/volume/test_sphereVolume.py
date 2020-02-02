import unittest
from sphereVolume import volume
from math import pi

class TestSphereVolume(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(volume(1), (4.0/3.0 * pi * 1))
        self.assertAlmostEqual(volume(0), 0.0)
        
    def test_values(self):
        self.assertRaises(ValueError,volume, -2)


    def test_types(self):
        # Makes sure type errors are raised when necessary
        self.assertRaises(TypeError, volume, 3+5j)
        self.assertRaises(TypeError, volume, True)
        self.assertRaises(TypeError, volume, "radius")