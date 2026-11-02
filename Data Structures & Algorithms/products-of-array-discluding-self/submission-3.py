class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffex = 1
        out = [1 for _ in nums]
        
        for i, n in enumerate(nums):
            out[i] *= suffex
            suffex *= n
        prefix = 1
        i = len(nums) - 1
        while i >= 0:
            out[i] *= prefix
            prefix *= nums[i]
            i -= 1
        # print(out)
        return out