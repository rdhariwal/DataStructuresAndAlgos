# You are given an array prices where prices[i] is the price of a given stock 
# on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

class Solution(object):

    def max_profit(self, prices):
        """
        : type prices: List[int]
        : rtype: int
        """
        maxProfit = 0
        l_ptr = 0
        r_ptr = 1
        while r_ptr <= len(prices) - 1:
            if prices[r_ptr] < prices[l_ptr]:
                l_ptr = r_ptr
            elif maxProfit < prices[r_ptr] - prices[l_ptr]:
                maxProfit = prices[r_ptr] - prices[l_ptr]
            r_ptr = r_ptr + 1

        return maxProfit


