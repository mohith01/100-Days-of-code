class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        str1 = []
        print(len(nums))
        for i in range(0,len(nums),2):
            str1+=nums[i]*[nums[i+1]]
            
        return str1
