class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        best = 0
        m = 0
        cur = "", 0
        charMap = {}
        for r in range(len(s)):
            c = s[r]
            if cur == ("", 0):
                cur = c, 1
            charMap[c] = charMap.get(c, 0) + 1
            if charMap[c] > cur[1]:
                cur = c, charMap[c]
            while r - l - charMap[cur[0]] >= k:
                # print(charMap, r)
                # print(cur)
                if charMap[c] >= cur[1]:
                    cur = c, charMap[c]
                charMap[s[l]] = charMap.get(s[l], 0) - 1
                cur = cur[0], charMap[cur[0]]
                l += 1
                if r - l-1 == charMap[c]:
                    break
            # print(s[l:r+1], r-l+1)
            best = max(best, r -l + 1)
        return best





















