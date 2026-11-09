class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in nums]
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for key, val in count.items():
            buckets[val-1].append(key)
        out = []
        i = len(buckets)-1
        while len(out) < k:
            out.extend(buckets[i])
            i-=1
        return out


# time O(3n) ~ O(n)
# space O(3n) ~ O(n)

