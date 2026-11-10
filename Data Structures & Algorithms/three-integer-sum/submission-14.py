class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return []
        r = len(nums) - 1
        l = 0
        out = set()
        i = 0
        while l<r:
            if nums[r] + nums[l] > target:
                r -= 1
            elif nums[r] + nums[l] < target:
                l += 1
            else:
                out.add((-target, nums[l], nums[r]))
                r -=1
                l += 1
        return out

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        setTupOut = set()
        nums = sorted(nums)
        for i, n in enumerate(nums):

            out = self.twoSum(nums[i+1:], -n)
            setTupOut.update(out)
        
        return [list(o) for o in setTupOut]



