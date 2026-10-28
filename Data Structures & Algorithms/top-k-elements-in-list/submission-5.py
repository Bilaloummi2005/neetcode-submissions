class Solution:
    def topKFrequent(self, nums, k: int):
        check = {}
        for n in nums:
            if check.get(n):
                check[n] += 1
            else:
                check[n] = 1
        sorted_check = list(dict(sorted(check.items(), key=lambda key: key[1])).keys())
        return sorted_check[len(sorted_check)-k:len(sorted_check)]
        