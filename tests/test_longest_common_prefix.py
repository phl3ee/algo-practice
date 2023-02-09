"""
Test via root directory with:
python -m unittest tests.<test_Case> -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

strs = ["abab","aba","abc"]
output = "ab"

"""
import unittest
from algos.longest_common_prefix import Solution

class TestTwoSum(unittest.TestCase):

    def test_example1(self):
        test   = Solution()
        strs   = ["flower","flow","flight"]
        output ="fl"
        result = test.longestCommonPrefix(strs)
        self.assertEqual(result,output)

    def test_example2(self):
        test   = Solution()
        strs   = ["dog","racecar","car"]
        output = ""
        result = test.longestCommonPrefix(strs)
        self.assertEqual(result,output)

    def test_example3(self):
        test   = Solution()
        strs   = ["dog"]
        output = "dog"
        result = test.longestCommonPrefix(strs)
        self.assertEqual(result,output)


    def test_example4(self):
        test   = Solution()
        strs   = ["abab","aba","abc"]
        output = "ab"
        result = test.longestCommonPrefix(strs)
        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()