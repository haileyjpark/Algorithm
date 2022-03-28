# Time: 68 ms (54.86%), Space: 14.7 MB (45.22%) - LeetHub
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx in range(len(nums)) :
            if (target <= nums[idx]) :
                return idx
        return len(nums)

# 다른 사람의 풀이
# Time: 52 ms (87.62%), Space: 14.9 MB (8.86%) - LeetHub
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
# 다른 사람의 풀이
# Time: 53 ms (79.46%), Space: 14.5 MB (99.00%) - LeetHub
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
