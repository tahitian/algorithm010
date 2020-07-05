from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        使用贪心算法，如果当天的价格大于前一天的价格，加上当天的价格差
        """
        profit = 0
        for i in range(len(prices)-1):
            profit += max(prices[i+1]-prices[i], 0)
        return profit

    def maxProfit_02(self, prices: List[int]) -> int:
        """
        一行代码写法
        """
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))