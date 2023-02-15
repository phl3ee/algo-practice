"""
Test with: python -m unittest tests.test_binary_string_add -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Given two binary strings a and b,
 return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

"""
import unittest
from algos.binary_string_add import Solution

class Test_addBinary(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        """
        test   = Solution()
        a      = "11"
        b      = "1"
        output = "100"
        result = test.addBinary(a, b)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        """
        test   = Solution()
        a      =  "1010"
        b      =  "1011"
        output = "10101"
        result = test.addBinary(a, b)
        self.assertEqual(result, output)

    def test_example3_padding1(self):
        """Example case from leetcode
        """
        test   = Solution()
        a      = "111"
        b      = "11111"
        output = "100110"
        result = test.addBinary(a, b)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()