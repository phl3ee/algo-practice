"""
Test with: python -m unittest tests.test_hash_table_phone_letters -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Given a string containing digits from 2-9 inclusive,
 return all possible letter combinations that the number could represent.
 Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons)
is given below. Note that 1 does not map to any letters.


Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

"""
import unittest
from algos.hash_table_phone_letters import Solution

class Test_letterCombinations(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        """
        test   = Solution()
        digits = "23"
        output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        result = test.letterCombinations(digits)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        """
        test   = Solution()
        digits = ""
        output = []
        result = test.letterCombinations(digits)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example case from leetcode
        """
        test   = Solution()
        digits = "2"
        output = ["a","b","c"]
        result = test.letterCombinations(digits)
        self.assertEqual(result, output)

    def test_example4(self):
        """Example case from leetcode
        """
        test   = Solution()
        digits = "233"
        output = ["ada","aea","afa","bda","bea","bfa","cda","cea","cfa"]
        result = test.letterCombinations(digits)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()