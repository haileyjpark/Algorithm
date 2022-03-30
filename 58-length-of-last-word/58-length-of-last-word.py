class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s[::-1].strip()
        for i in new_str:
            if ' ' not in new_str:
                return len(new_str)
            if i ==' ':
                return new_str.index(i)
            
        