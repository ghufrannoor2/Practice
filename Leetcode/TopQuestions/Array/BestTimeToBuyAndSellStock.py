
"""
Solution for Array: Best Time To Buy and Sell Stock Problem
"""

class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        print("\nArray - Best Time to Buy and Sell Stock:\n")
        print("\nPrices: " + str(prices) + "\n")
        
        maximum = 0
        for index, value in enumerate(prices):
            for i in range(len(prices) - index - 1):
                j = i + index + 1
                buy_price = value
                sell_price = prices[j]
                if sell_price - buy_price > maximum:
                    maximum = sell_price - buy_price
                    
        print("\nMaximum Profit: " + str(maximum) + "\n")
        return maximum

def run():
    solution = Solution()
    solution.max_profit([7, 1, 5, 3, 6, 4])

run()
