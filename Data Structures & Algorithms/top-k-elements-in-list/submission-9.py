class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {i:[] for i in range(1, len(nums)+1)}
        check = {}
        for n in nums:
            if check.get(n):
                check[n] += 1
            else:
                check[n] = 1
        for key, value in check.items():
            buckets[value].append(key)
        output = []
        i = len(nums)
        while len(output) < k:
            output.extend(buckets[i])
            i -= 1
        return output 


# space O(n)
#time O(n)