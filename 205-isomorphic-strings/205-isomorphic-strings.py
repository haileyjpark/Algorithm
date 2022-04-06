class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(list(s))) != len(set(list(t))):
            return False
        result = {}
        for i,j in zip(s,t):
            if i not in result:
                result[i] = j
            else:
                if result[i] != j:
                    return False
        return True