import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        b =  re.sub('[^0-9a-zA-Z]+', '', s)
        print(b.lower())
        return b.lower() == b.lower()[::-1]
