class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = False
        for i in range(2,len(arr)):
            if (arr[i]%2!=0) and (arr[i-1]%2!=0) and (arr[i-2]%2!=0):
                cnt = True
                break
                
        return cnt
                
