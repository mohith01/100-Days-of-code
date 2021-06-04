class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res=[]
        for i in candies:
            res.append((i+extraCandies)>=max(candies))
        return res   
