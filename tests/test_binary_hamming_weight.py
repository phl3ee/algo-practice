"""
Test with: python -m unittest tests.test_binary_hamming_weight -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Write a function that takes the binary representation of an unsigned integer and returns the number of 1 bits it has (also known as the Hamming weight).

Constraints:
The input must be a binary string of length 32.

Note, I think leetcode passes in the int as print(n) comes up with 11 and 128 for first examples

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

"""
import unittest
from algos.binary_hamming_weight import Solution

class Test_hammingWeight(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        """
        test   = Solution()
        n  = int('00000000000000000000000000001011', 2)
        output = 3
        result = test.hammingWeight(n)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        """
        test   = Solution()
        n  = int('00000000000000000000000010000000', 2)
        output = 1
        result = test.hammingWeight(n)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example case from leetcode
        """
        test   = Solution()
        n  = int('11111111111111111111111111111101', 2)
        output = 31
        result = test.hammingWeight(n)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()
