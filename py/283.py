#Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count =nums.count(0)
        for i in range(nums.count(0)):
            nums.remove(0)
                
        nums[:]  =nums + [0]*count
