"""
Solution for Array: Contains Duplicate Problem
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print("\nArray - Product Except Self:\n")
        print("\nNumbers: " + str(nums) + "\n")

        array = []

        for index, value in enumerate(nums):
            nums_copy = [num for num in nums]
            product = 1
            nums_copy.pop(index)
            
            for number in nums_copy:
                product = product * number
            
            array.append(product)
            
        
        print("\nProducts: " + str(array) + "\n")
        return array

def run():
    solution = Solution()
    solution.productExceptSelf([1, 2, 3, 4])

run()