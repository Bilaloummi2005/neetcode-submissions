class Solution:
    def twoSum(self, numbers, target: int):
        first = 0
        last = len(numbers) - 1
        while first < last:
            if numbers[first] + numbers[last] == target:
                return [first + 1, last +1]
            elif numbers[first] + numbers[last] > target:
                last -= 1
            else:
                first += 1
        return [0, 0]
