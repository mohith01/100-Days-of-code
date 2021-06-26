class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        max1 = 0
        for i in range(1,len(gain)+1):
            if sum(gain[:i])>max1:
                max1 = sum(gain[:i])
            
        return max1
