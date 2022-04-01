class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        nums = int(''.join(digits))
        nums += 1
        return list(str(nums))