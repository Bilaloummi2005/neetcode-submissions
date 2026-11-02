class Solution:
    def twoSumSorted(self, nums, target):
        first = 0
        last = len(nums)-1
        while first < last:
            cur = nums[first] + nums[last]
            if cur > target:
                last -= 1
            elif cur < target:
                first += 1
            else:
                return [first, last]
        return [0, 0]

    def threeSum(self, nums: [int]):
        sorted_nums = sorted(nums)
        out = []
        while len(sorted_nums) >= 3:
            n = sorted_nums[0]
            sorted_nums = sorted_nums[1:]
            f, l = [0,len(sorted_nums)]
            nums = sorted_nums[f:l]
            while [f, l] != [0,0]:
                nums = nums[f:l]
                target = -n
                f, l = self.twoSumSorted(nums, target)
                if [f, l] != [0, 0]:
                    out.append([n, nums[f], nums[l]])
        return [list(n) for n in set([tuple(n) for n in out])]










