from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = 1
        while i <= len(digits):
            #iterate list in reverse using a cheeky -1 multiplier
            if digits[-1 * i] < 9:
                digits[-1 * i] = digits[-1 * i] + 1
                return digits
            #we're here if value == 9,
            # so we need to zero and carry one more step
            digits[-1 * i] = 0
            i += 1
        #if we fall out the loop and still haven't returned,
        # last processed digit was a 9 so we need to add a
        # ten to the front of the list
        digits.insert(0,1)
        return digits
