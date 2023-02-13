class Solution:
    def climbStairs(self, n: int) -> int:

        # thus far we have 1=1, 2=2, 3=3, 4=5
        # so we are seeding a dictionary: {step:count..}
        # and the solution = step_count[n-1] + step_count[n - 2]
        # aka Fibonacci sequence
        step_count = {1:1, 2:2, 3:3}
        if n in step_count:
            return step_count[n]

        start = max(step_count.keys()) + 1
        for i in range(start, n + 1):
            print(i)
            step_count[i] = step_count[i - 2] + step_count[i - 1]
        return step_count[n]
