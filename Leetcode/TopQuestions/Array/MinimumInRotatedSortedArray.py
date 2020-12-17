class Solution(object):
    def find_minimum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        print("\nArray - Minimum in Rotated Sorted Array:\n")
        print("\nNums: " + str(nums) + "\n")
        
        # Store length
        n = len(nums)

        # Initialize
        end = n - 1
        if n % 2 == 0:
            middle = (n // 2)
        else:
            middle = (n - 1) // 2
        
        # Edge Cases
        if (n == 1):
            print("\nMinimum: " + str(nums[0]) + "\n")
            return nums[0]
        if nums[0] < nums[-1]:
            print("\nMinimum: " + str(nums[0]) + "\n")
            return nums[0]
        if nums[middle] < nums[middle - 1]:
            print("\nMinimum: " + str(nums[middle]) + "\n")
            return nums[middle]
        if nums[middle] > nums[middle + 1]:
            print("\nMinimum: " + str(nums[middle + 1]) + "\n")
            return nums[middle + 1]

        previous_value = nums[middle] # This is okay since middle cannot be the minimum now

        # Split the array in half
        if (nums[-1] < nums[middle]): # Search the right half
            for i in range(middle, end + 1):
                if previous_value > nums[i]:
                    minimum = nums[i]
                    break
                previous_value = nums[i]
        else: # Search the left half
            for i in range(0, middle + 1):
                if previous_value < nums[middle - i]:
                    minimum = previous_value
                    break
                previous_value = nums[middle - i]

        # Return
        print("\nMinimum: " + str(minimum) + "\n")
        return minimum

def run():
    solution = Solution()
    solution.find_minimum([6,1,2,3,4,5])

run()