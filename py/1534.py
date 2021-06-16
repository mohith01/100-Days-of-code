def check(tup1,tup2):#(i,j.k) ,(a,b,c)
    return True if ((abs(tup1[0]-tup1[1])<=tup2[0]) and (abs(tup1[1]-tup1[2]) <= tup2[1]) and (abs(tup1[2]-tup1[0]) <= tup2[2])) else False

print(check((3,0,1),(1,2,1)))
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                for k in range(j+1,len(arr)):
                    if check((arr[i],arr[j],arr[k]),(a,b,c)):
                        count+=1
                        
        return count
