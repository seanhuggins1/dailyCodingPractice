import unittest

class TestFindMax(unittest.TestCase):
    def test_A(self):
        self.assertEqual(findMaxSumSubarray([34,-50,42,14,-5,86]), 137)
        self.assertEqual(findMaxSumSubarray([-1,-3,-4,-4]), 0)
        self.assertEqual(findMaxSumSubarray([-2,-3,4,-1,-2,1,5,-3]), 7)


def findMaxSumSubarray(array):
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(array)):
        max_ending_here += array[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if (max_ending_here < 0):
            max_ending_here = 0
    return max_so_far

if __name__ == '__main__':
    unittest.main()