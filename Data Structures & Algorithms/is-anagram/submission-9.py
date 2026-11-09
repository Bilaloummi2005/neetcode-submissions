class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        for c in t:
            chars[c] = chars.get(c, 0) - 1
        for val in chars.values():
            if val != 0:
                return False
        return True