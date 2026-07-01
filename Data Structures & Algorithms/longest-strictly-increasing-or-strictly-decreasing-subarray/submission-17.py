class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def is_sorted(sub):
            i = 1
            j = 0
            while j < len(sub)-1:
                if sub[j] < sub[j+1]:
                    i+=1
                else:
                    i = 1
                j+=1
            if i == len(sub):
                return i
            j = 0
            while j < len(sub)-1:
                if sub[j] > sub[j+1]:
                    i+=1
                else:
                    i = 1
                j+=1
            if i == len(sub):
                return i
            return 1
        n = 1
        for i in range(len(nums)):
            j = 0
            i = i+1
            while j < len(nums):
                sub = nums[j:i+j]
                n = max(n, is_sorted(sub))
                j+=1
        
        return n