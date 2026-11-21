class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            n = n if n > 0 else -n
            nums[n-1] *= -1
            if nums[n-1] > 0:
                return n


# but we modify the array