class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0)>1:
            return True
        else:
            found=False
            for i in arr:
                if i*2  in arr and i!=0:
                    found=True
                    print(i)
                    break
        
            return found
