import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([-1, 2, 3, 4]), 4)
        self.assertEqual(max_list_iter([0, 2, 1, 0]), 2)
        self.assertEqual(max_list_iter([7, 2, 1, 5, 0]), 7)
        self.assertEqual(max_list_iter([9, 8, 7, 9]), 9)


    def test_reverse_rec(self):
        no_list = None
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        with self.assertRaises(ValueError):
            reverse_rec(no_list)
        self.assertEqual(reverse_rec([0, 0, 0]), [0, 0, 0])
        self.assertEqual(reverse_rec([0, 1, 1]), [1, 1, 0])
        self.assertEqual(reverse_rec([1, 0, 1]), [1, 0, 1])
        self.assertEqual(reverse_rec([-1, -2, 0]), [0, -2, -1])
            

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        list_val2 = []
        no_list = None
        low = 0
        high = len(list_val)- 1
        with self.assertRaises(ValueError):
            bin_search(0, 0, 1, no_list)
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(11, low, high, list_val), None)
        self.assertEqual(bin_search(-1, low, high, list_val), None)
        self.assertEqual(bin_search(9, low, high, list_val), 7)
        self.assertEqual(bin_search(0, low, high, list_val2), None)
        self.assertEqual(bin_search(1, 1, 2, list_val), 1)


if __name__ == "__main__":
        unittest.main()

    
