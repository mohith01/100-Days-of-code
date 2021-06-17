class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        arr.sort()
        diff  =arr[-1]
        for i in range(len(arr)-1):
            if (arr[i+1]-arr[i])<diff and (arr[i+1]>arr[i]):
                diff = arr[i+1]-arr[i]
                
        for j in range(len(arr)-1):
            if (arr[j+1]-arr[j])==diff:
                res.append([arr[j],arr[j+1]])
                
        return res
