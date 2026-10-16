class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ids = {}
        for i, n in enumerate(nums):

            if target - n in ids:
                return [ids[target - n], i]
            ids[n] = i

# time O(n)
#space O(n)
#simplifyed with the help of gpt
