
"""
Solution for Array: Maximum Sub-Array Problem
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print("\nArray - Maximum Sub-Array:\n")
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
                sublist_sum = sum(sublist)

                if not first_run: # Check if not first run
                    if sublist_sum > max_sum:
                        max_sum = sublist_sum
                        
                else: # If first run, set max_sum for first time
                    first_run = False
                    max_sum = sublist_sum
                
        print("\nMax Sum: " + str(max_sum) + "\n")
        return max_sum

def run():
    solution = Solution()
    solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])

run()
