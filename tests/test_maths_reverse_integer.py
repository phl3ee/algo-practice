"""
Test with: python -m unittest tests.test_maths_reverse_integer -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Given a signed 32-bit integer x, return x with its digits reversed.
 If reversing x causes the value to go outside
 the signed 32-bit integer range [-2e31, 2e31 - 1], then return 0.
 Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

"""
import unittest
from algos.maths_reverse_integer import Solution

class Test_reverse(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = 123
        output = 321
        result = test.reverse(x)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = -123
        output = -321
        result = test.reverse(x)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example case from leetcode
        """
        test   = Solution()
        x      = 120
        output = 21
        result = test.reverse(x)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()