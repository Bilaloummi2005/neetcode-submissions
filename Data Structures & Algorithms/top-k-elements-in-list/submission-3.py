class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appear = {}
        for i in nums:
            if appear.get(i):
                appear[i] += 1
            else:
                appear[i] = 1
        result = sorted(appear.items(), key = lambda items: items[1])
        result = [res[0] for res in result]
        return result[len(result)-k:len(result)]

