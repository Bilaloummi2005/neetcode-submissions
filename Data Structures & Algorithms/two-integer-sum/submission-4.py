class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ids = {}
        for i, n in enumerate(nums):
            if ids.get(n , -1) != -1:
                ids[n].append(i)
            else:
                ids[n] = [i]

            if ids.get(target - n, -1) != -1:
                if ids[target - n][0] == i:
                    if len(ids[target - n]) > 1:
                        return [ids[target - n][0], i]
                    continue
                return [ids[target - n][0], i]


# time O(n)
#space O(n)
