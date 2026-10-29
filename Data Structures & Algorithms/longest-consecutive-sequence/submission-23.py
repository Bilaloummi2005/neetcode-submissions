class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        setNums = set(nums)
        l = 1
        for n in setNums:
            c = 1
            if n-1 in setNums:
                continue
            while n+1 in setNums:
                c += 1
                n += 1
            l = max(c, l)
        return l

# space O(n)
# time O(n)
