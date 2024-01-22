class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            complement = target - num
            if complement in d:
                return i, d[complement]
            d[num] = i
            i += 1