from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)


    def remove_duplicates_pointers(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow + 1] = nums[fast]
                fast += 1
                slow += 1

        return slow + 1
