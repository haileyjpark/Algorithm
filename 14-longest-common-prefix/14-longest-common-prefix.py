class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x)) 
        
        if len(strs) == 0:
            return
        else:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i]
            return strs[0]
        
        
# 다른 사람의 풀이 => binary search
class Solution2:
    def longestCommonPrefix2(self, strs : List[str]) -> str:
        if len(strs) == 0:
            return
        else:
            target = strs[0]
            remains = strs[1:]
            if not ramains:
                return target
            left = 0
            right = len(target) - 1
            mid = ((left + right) // 2)
            
            while left <= right:
                if self.isCommonPrefix(target[:mid + 1], remains):
                    left = mid + 1
                else:
                    right = mid - 1
                mid = ((left + right) // 2)
           return target[:mid + 1]
    
    
    def isCommonPrefix(self, target, remains):
        for x in remains:
            if not x.startswith(target):
                return False
            return True
        
        
# 다른 사람의 풀이 => divide and conquer
class Solution3:
    def commonPrefix2(self, str1, str2):
        result = ''
        i, j = 0, 0
        
        while i <= len(str1) - 1 and j <= len(str2) - 1:
            if str1[i] != str2[j]:
                break
            result += str1[i]
            i, j = i + 1, j + 1
        return result
    
    def longestCommonPrefixHelp(self, strs: List[str], low: int, high: int) -> str:
        if low == high:
            return strs[low]
        if high > low:
            mid = low + (high - low) // 2
            
            str1 = self.longestCommonPrefixHelp(strs, low, mid)
            str2 = self.longestCommonPrefixHelp(strs, mid + 1, high)
            
            return self.commonPrefix(str1, str2)
        
    def longestCommonPrefix3(self, strs: List[str]) => str:
        if len(strs) == 0:
            return
        return self.longestCommonPrefixHelp(strs, 0, len(strs) - 1)
