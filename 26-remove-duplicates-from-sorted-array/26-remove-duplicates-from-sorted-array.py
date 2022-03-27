# Time: 6375 ms (5.03%), Space: 15.5 MB (67.71%) - LeetHub
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            while nums.count(num) > 1:
                nums.remove(num)
        return len(nums)
        
        
# 다른 사람의 풀이
# Time: 76 ms (99.77%), Space: 15.6 MB (67.71%) - LeetHub
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        change_index = 1
        for i in range(0, len(nums)):
            if i !=0 and nums[i-1] != nums[i]:
                nums[change_index] = nums[i]
                change_index += 1
        
        return change_index
