class Solution:
    def reverse(self, x: int) -> int:
        out = 0
        #convert string > list
        int_list = list(str(x))

        #reverse the list
        int_list.reverse()

        #if last char is '-' pop it off and put back
        # on left of list
        if int_list[-1] == "-":
            int_list.insert(0, int_list.pop())

        out = int(''.join(int_list))
        if abs(out) > (2 << 31 - 1):
            return 0
        return out
