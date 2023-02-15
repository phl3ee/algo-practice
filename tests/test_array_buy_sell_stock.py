"""
Test with: python -m unittest tests.test_array_buy_sell_stock -v
e.g. python -m unittest tests.test_longest_common_prefix -v

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""
import unittest
from algos.array_buy_sell_stock import Solution

class Test_maxProfit(unittest.TestCase):
    """ Unit tests for leetcode fun and games
    """

    def test_example1(self):
        """Example case from leetcode
        Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is
        not allowed because you must buy before you sell.
        """
        test   = Solution()
        prices = [7,1,5,3,6,4]
        output = 5
        result = test.maxProfit(prices)
        self.assertEqual(result, output)

    def test_example2(self):
        """Example case from leetcode
        In this case, no transactions are done and the max profit = 0.
        """
        test   = Solution()
        prices = [7,6,4,3,1]
        output = 0
        result = test.maxProfit(prices)
        self.assertEqual(result, output)

    def test_example3(self):
        """Example case from leetcode
        """
        test   = Solution()
        prices = [1,2]
        output = 1
        result = test.maxProfit(prices)
        self.assertEqual(result, output)

if __name__ == '__main__':
    unittest.main()