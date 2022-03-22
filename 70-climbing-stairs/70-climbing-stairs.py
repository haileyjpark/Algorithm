class Solution:
    def climbStairs(self, n: int) -> int:
        result = [j for j in range(n+1)]
        
        for i in range(3, n+1):
            result[i] = result[i-1] + result[i-2]
        
        return result[n]