class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums)): #4 1,2,3
            list1.append(sum(nums[:i+1]))
        return list1
