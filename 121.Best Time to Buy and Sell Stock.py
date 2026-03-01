"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1: create a new list every iteration and scan it with min O(n^2) 
        # max_profit = 0
        # for i in range(1, len(prices)):
        #     max_profit = max(max_profit, prices[i] - min(prices[:i]))
        # return max_profit
        # Solution 2: Just use min/max and store min_price instead of looping over entire array:
        max_profit = 0
        min_buy_price_so_far = prices[0]
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_buy_price_so_far)
            min_buy_price_so_far = min(min_buy_price_so_far, prices[i])
        return max_profit
            

        
