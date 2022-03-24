class Solution:
    def isPalindrome(self, x: int) -> bool:
        if '-' in str(x):
            return False
        if list(str(x)) == list(reversed(str(x))):
            return True
        else:
            return False
        