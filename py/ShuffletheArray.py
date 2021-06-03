class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(n): #[0,1,2]
            arr.append(nums[i])
            arr.append(nums[((i+n)%len(nums))])      
        return arr
        
