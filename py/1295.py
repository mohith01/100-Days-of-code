class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count1  =0 
        for i in nums:
            if len(str(i))%2==0:
                count1+=1
                
        return count1
