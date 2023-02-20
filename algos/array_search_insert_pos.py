from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        #no-ops, return if present
        if target in nums:
            return nums.index(target)

        highend = len(nums) - 1
        middle = 0
        lowend = 0

        #no-ops,
        # bolt it on the upper/mid/lower bounds if not present
        if nums[highend] < target:
            return highend + 1
        if nums[0] > target:
            return 0
        if len(nums) == 2:
            return 1

        #if no value, binary search the list
        while lowend < highend:
            middle = (highend + lowend) // 2
            if nums[middle] < target:
                lowend = middle + 1
            else:
                highend = middle

        return lowend
