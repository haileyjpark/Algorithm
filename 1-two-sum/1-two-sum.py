class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            

# 다른 사람의 풀이 [two-pass Hash Table]
class Solution2(object):
    def twoSum2(self, nums, target):
        table = {num: i for i, num in enumerate(nums)}

        for i, num in enumerate(nums):
            if ((target-num) in table) and (i != table[(target-num)]):
                return [i, table[(target-num)]]
            

# 다른 사람의 풀이 [one-pass Hash Table]
class Solution3(object):
    def twoSum3(self, nums, target):
        table = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in table:
                return [i, table[complement]]
            else:
                table[num] = i
