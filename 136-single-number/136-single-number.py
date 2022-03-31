# Time: 9429 ms (5.00%), Space: 16.8 MB (53.50%) - LeetHub
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
            
# 다른 사람의 풀이
# Time: 116 ms (99.62%), Space: 16.6 MB (85.18%) - LeetHub
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer = answer ^ num
        return answer
