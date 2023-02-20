from math import floor,sqrt

class Solution:
    def mySqrt(self, x: int) -> int:
        y = 1
        rolling = 0
        while x != (y * y):
            rolling = y * y
            if rolling > x:
                return y - 1
            y += 1
        return y

    def mySqrt_fast(self, x: int) -> int:
        return floor(sqrt(x))
