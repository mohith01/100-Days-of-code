class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        d = len(arr)*5//100
        
        
        return sum(arr[d:-d])/len(arr[d:-d])
