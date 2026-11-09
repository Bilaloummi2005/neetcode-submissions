class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        s_set = set()
        for r in range(len(s)):
            c = s[r]
            while c in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(c)
            best = max(best, r - l+1)
        return best


# time O(n)
# space O(m)
