"""
Test with: python -m unittest tests.test_search_insert_pos -v
e.g. python -m unittest tests.test_longest_common_prefix -v

Given a sorted array of distinct integers and a target value,
 return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

"""
import unittest
from algos.search_insert_pos import Solution

class Test_def(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        """
        test   = Solution()
        nums = [1,3,5,6]
        target = 5
        output = 2
        result = test.searchInsert(nums, target)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        """
        test   = Solution()
        nums = [1,3,5,6]
        target = 2
        output = 1
        result = test.searchInsert(nums, target)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example case from leetcode
        """
        test   = Solution()
        nums = [1,3,5,6]
        target = 7
        output = 4
        result = test.searchInsert(nums, target)
        self.assertEqual(result, output)

    def test_example4(self):
        """Example case from leetcode
        """
        test   = Solution()
        nums = [1,3,5,6]
        target = 0
        output = 0
        result = test.searchInsert(nums, target)
        self.assertEqual(result, output)

    def test_example5(self):
        """Example case from leetcode
        """
        test   = Solution()
        nums = [1,3]
        target = 2
        output = 1
        result = test.searchInsert(nums, target)
        self.assertEqual(result, output)

    def test_example6(self):
        """Example case from leetcode
        """
        test   = Solution()
        nums = [1,3,5]
        target = 4
        output = 2
        result = test.searchInsert(nums, target)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()