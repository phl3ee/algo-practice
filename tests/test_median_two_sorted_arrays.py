"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""
import unittest
from algos.maths_median_two_sorted_arrays import Solution

class TestMedianSortedArrays(unittest.TestCase):

    def test_example1(self):
        solution = Solution()
        nums1 = [1,3]
        nums2 = [2]
        output = 2.0
        result = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, output)

    def test_example2(self):
        solution = Solution()
        nums1 = [1,2]
        nums2 = [3,4]
        output = 2.5
        result = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()