class Solution:
    def isPalindrome(self, x: int) -> bool:
        if '-' in str(x):
            return False
        if list(str(x)) == list(reversed(str(x))):
            return True
        else:
            return False
        
# Time: 64 ms (85.83%), Space: 14 MB (9.15%) - LeetHub



# 다른 사람의 풀이
class Solution2:
    def isPalindrome2(self, x: int) -> bool:
        x = list(str(x))
        
        return x == x[::-1]
# Time: 76 ms (69.87%), Space: 13.9 MB (67.38%) - LeetHub
