class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #Edge cases entry check
        #is it an empty string? just leave man
        if len(s) == 0:
            return 0
        #is it single char, or is it all the same char?
        #if so, exit early with a 1
        if len(s) == 1 or all(ch == s[0] for ch in s):
            return 1

        output = 0
        visited = [0] * 256
        for i in range(len(s)):
            visited = [0] * 256
            for nextChar in range(i, len(s)):
                    if (visited[ord(s[nextChar])] == True):
                        break
                    else:
                        output = max(output, nextChar - i + 1)
                        visited[ord(s[nextChar])] = True

        return output

    def lengthOfLongestSubstring_fast(self, s: str) -> int:
        ans = 0
        usedCharacters = {}
        leftPointer = 0

        # A left pointer will start at index 0, when a duplicate character is found
        # the pointer will be updated to the index after the first of the duplicates.
        # Length is calcualted each time a new non duplicate is added.

        # The pointer should not move backwards, if we find a duplicate , but the duplicate
        # character is no longer in our substring, because another update occured, we want
        # to leave our pointer as is.

        for i, val in enumerate(s):
            if val in usedCharacters:
                if usedCharacters[val] + 1 > leftPointer:
                    leftPointer = usedCharacters[val] + 1

            usedCharacters[val] = i


            # Calculate the length of our current substring
            lengthSub = i + 1 - leftPointer
            if ans < lengthSub:
                ans = lengthSub

        return ans