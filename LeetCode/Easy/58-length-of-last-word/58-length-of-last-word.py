class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s[::-1].strip()
        for i in new_str:
            if ' ' not in new_str:
                return len(new_str)
            if i ==' ':
                return new_str.index(i)
            

# 다른 사람의 풀이 (split 사용)
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
    
# 다른 사람의 풀이 (reversed 사용)
class Solution3:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in reversed(s.strip()):
            if c == " ":
                break
            count += 1
        return count
    
# 다른 사람의 풀이 (최대 index 사용)
class Solution4:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        string = s.strip()
        for i in range(len(string)-1, -1, -1):
            if string[i] == " ":
                break
            count += 1
        return count
