class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for c in s:
            if not chars.get(c):
                chars[c] =1
                continue
            chars[c] += 1
        for c in t:
            if not chars.get(c):
                return False
            chars[c] -= 1
        for _, val in chars.items():
            if val == 0:
                pass
            else:
                return False
        return True
        