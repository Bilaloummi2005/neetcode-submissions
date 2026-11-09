class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        count = 0
        for n in nums:
            if (n-1) in setNums:
                continue
            i = 1
            while (n+1) in setNums:
                n +=1
                i += 1
            count = max(count, i)
        return count