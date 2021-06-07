class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b = digits
        return list(map(int,str(int(''.join(map(str,b)))+1)))
