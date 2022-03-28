class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx in range(len(nums)) :
            if (target <= nums[idx]) :
                return idx
        return len(nums)
