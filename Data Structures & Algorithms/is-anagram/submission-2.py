class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for c in s:
            if chars.get(c):
                chars[c] += 1
            else:
                chars[c] = 1
        for c in t:
            if chars.get(c):
                chars[c] -= 1
            else:
                return False
        for c in chars.values():
            if  c != 0:
                return False
        return True