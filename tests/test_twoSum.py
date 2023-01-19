"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
import unittest
from algos import twoSum, twoSumFast

class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        nums = [2,7,11,15]
        target = 9
        result = twoSum(nums,target)
        self.assertEqual(result,[0,1])

    def test_example2(self):
        nums = [3,2,4]
        target = 6
        output = [1,2]
        result = twoSum(nums,target)
        self.assertEqual(result,output)

    def test_example3(self):
        nums = [3,3]
        target = 6
        output = [0,1]
        result = twoSum(nums,target)
        self.assertEqual(result,output)

    def test_example3Fast(self):
        nums = [3,3]
        target = 6
        output = [0,1]
        result = twoSumFast(nums,target)
        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()