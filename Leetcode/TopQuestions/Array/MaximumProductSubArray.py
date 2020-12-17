
"""
Solution for Array: Maximum Product Sub-Array Problem
"""

class Solution(object):
    def max_product(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print("\nArray - Maximum Product Sub-Array:\n")
        print("\nNums: " + str(nums) + "\n")
        
        # Store length
        list_length = len(nums)
        
        # Initialize
        first_run = True
        
        # Iterate through length
        for i in range(list_length):
            sublist_length = list_length - i
            num_sublists = (list_length - sublist_length) + 1

            for i in range(num_sublists):
                sublist = nums[i:sublist_length + i]
                sublist_product = 1
                for number in sublist:
                    sublist_product = sublist_product * number

                if not first_run: # Check if not first run
                    if sublist_product > maximum_product:
                        maximum_product = sublist_product
                        
                else: # If first run, set maximum_product for first time
                    first_run = False
                    maximum_product = sublist_product
                
        print("\nMax Product: " + str(maximum_product) + "\n")
        return maximum_product

def run():
    solution = Solution()
    solution.max_product([2, 3, -2, 4])

run()
