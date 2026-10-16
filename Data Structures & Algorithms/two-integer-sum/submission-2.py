class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ids = {}
        for i, n in enumerate(nums):
            if ids.get(n , -1) != -1:
                ids[n].append(i)
            else:
                ids[n] = [i]

            if ids.get(target - n, -1) != -1:# 7 - 3 = 4
                print(ids[target - n] == i)
                if ids[target - n][0] == i:
                    if len(ids[target - n]) > 1:
                        return [ids[target - n][0], i]
                    continue
                return [ids[target - n][0], i]

        print(ids)
        return [0, 1]
