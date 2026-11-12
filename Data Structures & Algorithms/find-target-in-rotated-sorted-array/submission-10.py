class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = (r+l)//2
            # print(nums[l:r+1])
            # print("mid:", nums[mid], ":l:", nums[l], ":r:", nums[r], ":target:", target)
            if nums[mid] == target:
                return mid
            # if nums[r] == target:
            #     return r
            # if nums[l] == target:
            #     return l
            if nums[l] <= nums[mid]:
                if target <= nums[mid] and target >= nums[l]:
                    r = mid -1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if target <= nums[r] and target >= nums[mid]:
                    l = mid +1
                else:
                    r = mid - 1
            else:
                return -1





        return -1