from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = ""
        inputsize = len(strs)

        #no-op checks:
        if inputsize == 0:
            return result
        #is there only one item, return whole item (or nothing?)
        if inputsize == 1:
            return strs[0]

        #max common string is the length of shortest item
        strs.sort()
        maxlength = min(len(strs[0]), len(strs[-1]))
        i = 0
        while ( i < maxlength and strs[0][i] == strs[inputsize - 1][i]):
            i += 1

        result = strs[0][0:i]
        return result
