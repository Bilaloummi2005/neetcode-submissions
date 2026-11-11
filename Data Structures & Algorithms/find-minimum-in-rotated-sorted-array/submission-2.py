class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        i = 0
        while l<=r:
            i += 1
            mid = (l + r) // 2
            # print(nums[r], nums[l], nums[mid], r, l, mid)
            if nums[mid] < nums[r] and nums[mid] < nums[l] and l == r-1-1:
                return nums[mid]
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid+1
        return nums[mid]