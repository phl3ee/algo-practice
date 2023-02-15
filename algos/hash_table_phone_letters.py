from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []

        #number_map
        number_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        #initialise the output list and seed it
        # return if only one digit supplied
        output = []
        if len(digits) == 1:
            return number_map[digits[0]]
        output = number_map[digits[0]]

        #helper function that joins two lists
        def join_lists(list1, list2):
            out = []
            for i in list1:
                for j in list2:
                    out.append(i + j)
            return out

        for i in digits[1:]:
            output = join_lists(output, number_map[i])

        return output
