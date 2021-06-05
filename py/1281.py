class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1 = 0
        prod = 1
        for i in list(str(n)):
            sum1=sum1+int(i)
            prod=prod*int(i)
        return prod-sum1
        
