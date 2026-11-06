from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        out = []
        queue = deque()
        for r in range(len(nums)):
            n = nums[r]
            while queue and n > queue[-1][0]:
                test = queue.pop()

            queue.append((n, r))
            if r-l+1 == k:
                big, i = queue[0]
                if i == l:
                    queue.popleft()
                out.append(big)
                l+=1
        return (out)



# time O(n)
# space O(n)






        