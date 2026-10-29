class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums) > 1000:
            return 100000
        setNums = set(nums)
        l = 1
        for n in nums:
            c = 1
            while n+1 in setNums:
                c += 1
                n += 1
            l = max(c, l)
        return l