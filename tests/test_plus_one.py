"""
Test with: python -m unittest tests.<test_Case> -v
e.g. python -m unittest tests.test_longest_common_prefix -v

You are given a large integer represented as an integer array digits,
 where each digits[i] is the ith digit of the integer.
 The digits are ordered from most significant to least significant in left-to-right order.
 The large integer does not contain any leading 0s.
 Increment the large integer by one and return the resulting array of digits.


Example 1:

Input: <INPUT_1>
Output: <OUTPUT_1>

Example 2:

Input: strs = <INPUT_2>
Output: <OUTPUT_2>
Explanation: <EXPLANATION_2>

"""
import unittest
from algos.maths_plus_one import Solution

class Test_plusOne(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """
    def test_example1(self):
        """Example 1"""
        test   = Solution()
        digits = [1,2,3]
        output = [1,2,4]
        result = test.plusOne(digits)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example 2"""
        test   = Solution()
        digits = [4,3,2,1]
        output = [4,3,2,2]
        result = test.plusOne(digits)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example 3"""
        test   = Solution()
        digits = [9]
        output = [1,0]
        result = test.plusOne(digits)
        self.assertEqual(result, output)

    def test_example4_single_item(self):
        """Example 4"""
        test   = Solution()
        digits = [8]
        output = [9]
        result = test.plusOne(digits)
        self.assertEqual(result, output)

    def test_example5_carry_10s(self):
        """Can I carry tens?"""
        test   = Solution()
        digits = [1,9]
        output = [2,0]
        result = test.plusOne(digits)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()