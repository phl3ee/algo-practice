from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #merge lists and sort, keep nums1
        nums1.extend(nums2)
        nums1.sort()

        #we only want the middle two values
        # if no modulo 2, return middle value
        length = len(nums1)
        if length % 2 != 0:
            return nums1[length // 2] / 1
        #otherwise take elements either side of middle and divide
        else:
            return (nums1[length // 2 - 1] + nums1[length // 2]) / 2


