class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = 0
        l = len(numbers) - 1
        while r < l:
            val = numbers[r] + numbers[l]
            if target > val:
                r += 1
            elif target < val:
                l -= 1
            else:
                return [r + 1, l + 1]
