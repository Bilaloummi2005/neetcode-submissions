class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) < 1:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        first = 0
        last = len(nums) - 1
        while first <= last:
            midl = int(first/2 + last/2)
            if nums[midl] == target:
                return midl
            if target > nums[midl]:
                first = midl
            elif target < nums[midl]:
                last = midl
            if first == last - 1:
                if nums[first] == target:
                    return first
                elif nums[last] == target:
                    return last
                return -1
            if first == last:
                if nums[first] == target:
                    return first
                return -1
            

        return -1
    