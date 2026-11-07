class Solution:
    def search(self, nums: List[int], target: int) -> int:

        right = 0
        left = len(nums)-1
        i = 0
        while True:
            if right == left-1 or right == left:
                if nums[right] == target:
                    return right
                if nums[left] == target:
                    return left
                return -1
            midl = int((left + right)/2)
            if target > nums[midl]:
                right = midl+1
            elif target < nums[midl]:
                left = midl-1
            else:
                return midl
            i+=1
        return -1



# time O(logn)
# space O(1)
