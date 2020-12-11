"""
Solution for Array: Contains Duplicate Problem
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        print("\nArray - Contains Duplicate:\n")
        print("\nNumbers: " + str(nums) + "\n")
        
        for index, value in enumerate(nums):
            for i in range(len(nums) - index - 1):
                j = i + index + 1
                first = value
                second = nums[j]
                if first == second:
                    print("\nContains Duplicate\n")
                    return True
        
        print("\nDoesn't Contain Duplicate\n")
        return False

def run():
    solution = Solution()
    solution.containsDuplicate([1, 2, 3, 1])

run()