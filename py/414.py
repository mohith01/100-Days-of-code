class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        else:
            nums1 = nums.copy()
            for i in range(2):
                max1 = max(nums)
                while max1 in nums:
                    nums.remove(max1)
                if len(nums)==0:
                    break
            if len(nums)==0:
                return max(nums1)
            else:
                return max(nums)
        
