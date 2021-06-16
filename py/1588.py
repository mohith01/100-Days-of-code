class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum1 = 0
        for i in range(len(arr)):
            if i%2==0:
                pass
            else:
                for j in range(len(arr)-i+1): 
                    sum1+=sum(arr[j:i+j])
                    
        if len(arr)%2==0:
            return sum1
        else:
            return sum1+sum(arr)
                            
