"""
Test with: python -m unittest tests.test_climb_stairs -v
e.g. python -m unittest tests.test_longest_common_prefix -v

You are climbing a staircase.
 It takes n steps to reach the top.
 Each time you can either climb 1 or 2 steps.
 In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""
import unittest
from algos.climb_stairs import Solution

class Test_climbStairs(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        """
        test   = Solution()
        n      = 2
        output = 2
        result = test.climbStairs(n)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        """
        test   = Solution()
        n      = 3
        output = 3
        result = test.climbStairs(n)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example case from leetcode
        """
        test   = Solution()
        n      = 4
        output = 5
        result = test.climbStairs(n)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()