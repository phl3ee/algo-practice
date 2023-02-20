"""
Test with: python -m unittest tests.<test_Case> -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Given a non-negative integer x,
 return the square root of x rounded down to the nearest integer.
 The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since we round it down to the nearest integer, 2 is returned.

"""
import unittest
from algos.maths_sqrt_x import Solution

class Test_mySqrt(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = 4
        output = 2
        result = test.mySqrt(x)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = 9
        output = 3
        result = test.mySqrt(x)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = 8
        output = 2
        result = test.mySqrt(x)
        self.assertEqual(result, output)

    def test_example1_fast(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = 4
        output = 2
        result = test.mySqrt_fast(x)
        self.assertEqual(result, output)

    def test_example2_fast(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = 9
        output = 3
        result = test.mySqrt_fast(x)
        self.assertEqual(result, output)

    def test_example3_fast(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = 8
        output = 2
        result = test.mySqrt_fast(x)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()