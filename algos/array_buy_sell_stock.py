from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """prices = [7,1,5,3,6,4]
        out == 5
        """
        #check empty list
        if prices is None:
            return 0
        #all same number
        if len(set(prices)) == 1:
            return 0

        list_length = len(prices)
        max_profit  = 0
        buy_low     = prices[0]

        for i in range(1, list_length):
            new_profit = prices[i] - buy_low
            if new_profit > max_profit:
                max_profit = new_profit
            if prices[i] < buy_low:
                buy_low = prices[i]
        return max_profit
