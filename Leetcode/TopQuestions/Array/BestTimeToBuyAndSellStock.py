
"""
Solution for Array: Best Time To Buy and Sell Stock Problem
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        print("\nArray - Best Time to Buy and Sell Stock:\n")
        print("\nPrices: " + str(prices) + "\n")
        
        max = 0
        for index, value in enumerate(prices):
            for i in range(len(prices) - index - 1):
                j = i + index + 1
                buy_price = value
                sell_price = prices[j]
                if sell_price - buy_price > max:
                    max = sell_price - buy_price
                    
        print("\nMax Profit: " + str(max) + "\n")
        return max

def run():
    solution = Solution()
    solution.maxProfit([7, 1, 5, 3, 6, 4])

run()
