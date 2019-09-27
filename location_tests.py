import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    # Add more tests!

    def test_eq_diff_latlon(self):
        """testing the eq to make sure that, with different latitudes and the same 
        longitudes and vice versa, the locations will not be equal"""
        loc1 = Location("SLO", 45.7, -40.2)
        loc2 = Location("SLO", 45.7, 0.0)
        loc3 = Location("SLO", 60.2, -40.2)
        loc4 = Location("SLO", 45.7, -40.2)
        self.assertNotEqual(loc1, loc2)
        self.assertEqual(loc1, loc4)
        self.assertNotEqual(loc3, loc4)


    def test_eq_diff_loc(self):
        """test having the same latitute and longitudes at different locations"""
        loc1 = Location("Shingle Springs", 20.0, 47.9)
        loc2 = Location("Pismo", 20.0, 47.9)
        loc3 = Location("SLO", 20.0, 47.9)
        loc4 = Location("SLO", 20.0, 47.9)
        self.assertNotEqual(loc1, loc4)
        self.assertNotEqual(loc2, loc4)
        self.assertEqual(loc3, loc4)


if __name__ == "__main__":
        unittest.main()
