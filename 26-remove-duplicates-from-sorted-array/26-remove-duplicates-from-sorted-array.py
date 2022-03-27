class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for num in nums:
        #     while nums.count(num) > 1:
        #         nums.remove(num)
        # return len(nums)
        if len(nums) == 0:
            return 0
        change_index = 1
        for i in range(0, len(nums)):
            if i !=0 and nums[i-1] != nums[i]:
                nums[change_index] = nums[i]
                change_index += 1
        
        return change_index
