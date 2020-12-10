class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print("\nArray - Two Sum:\n")
        print("\nNumbers: " + str(nums) + "\n")
        print("\nTarget: " + str(target) + "\n")
        
        for index, number in enumerate(nums):
            print("First Index: " + str(index) + "\n")
            for i in range(len(nums) - index - 1):
                print("Second Index: " + str(i) + "\n")
                j = len(nums) - 1 - i
                print("Second Index (Modified): " + str(j) + "\n")
                if nums[index] + nums[j] == target:
                    print("First Number: " + str(nums[index]) + "\n")
                    print("Second Number: " + str(nums[index]) + "\n")
                    print("Sum: " + str(nums[index] + nums[j]) + "\n")
                    print("Target: " + str(target) + "\n")
                    return [index, j]

def run():
    solution = Solution()
    solution.twoSum([2, 7, 11, 15], 9)

run()