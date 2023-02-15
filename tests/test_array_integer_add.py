"""
Test with: python -m unittest tests.test_array_integer_add -v
e.g. python -m unittest tests.test_longest_common_prefix -v

The array-form of an integer num is an array representing its digits in left to right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

"""
import unittest
from algos.array_integer_add import Solution

class Test_addToArrayForm(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        Explanation: 1200 + 34 = 1234
        """
        test   = Solution()
        num    = [1,2,0,0]
        k      = 34
        output = [1,2,3,4]
        result = test.addToArrayForm(num, k)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        Explanation: 274 + 181 = 455
        """
        test   = Solution()
        num    = [2,7,4]
        k      = 181
        output = [4,5,5]
        result = test.addToArrayForm(num, k)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example case from leetcode
        Explanation: 215 + 806 = 1021
        """
        test   = Solution()
        num    = [2,1,5]
        k      = 806
        output = [1,0,2,1]
        result = test.addToArrayForm(num, k)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()