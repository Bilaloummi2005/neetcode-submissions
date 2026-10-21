class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if seen.get(target - n) is not None:
                return [seen.get(target - n), i]
            seen[n] = i