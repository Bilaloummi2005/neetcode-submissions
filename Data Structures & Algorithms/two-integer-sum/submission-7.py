class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, n in enumerate(nums):
            if my_dict.get(target - n) is not None :
                return [my_dict[target - n], i]
            my_dict[n] = i
        