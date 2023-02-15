from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        #no-ops
        if k == 0:
            return num
        #turn the list into a concatenated int and add k
        total = int(''.join([str(x) for x in num])) + k
        return [int(i) for i in str(total)]
