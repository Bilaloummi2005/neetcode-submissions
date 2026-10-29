class Solution:
    def productExceptSelf(self, nums):
        prefix = [n for n in nums]
        suffix = prefix.copy()
        i = 0
        j = len(nums)  -1
        while i < len(nums):
            if i <= 0:
                prefix[i] *= 1
            else:
                prefix[i] *= prefix[i-1]
            if j >= len(nums) - 1:
                suffix[j] *= 1
            else:
                suffix[j] *= suffix[j + 1]
            i += 1
            j -= 1
        output = [1 for _ in nums]
        
        i = 0
        while i < len(nums):
            output[i] = (prefix[i - 1] if i > 0 else 1) * (suffix[i + 1] if i <len(nums) - 1 else 1)
            i += 1
        
        return (output)