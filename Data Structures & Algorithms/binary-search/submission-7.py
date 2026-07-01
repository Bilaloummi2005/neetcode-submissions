class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums) - 1
        i = 0
        
        mid = int(f/2 + l/2)
        print(nums[mid], target, mid, l, f)
        while l > f:
            mid = int(f/2 + l/2)
            print(nums[mid], target, mid, l, f)
            if nums[mid] > target:
                l = mid
            elif nums[mid] < target:
                f = mid + 1
            else:
                return mid
            i+=1
        if l == f and nums[f] == target:
            return f
        return -1