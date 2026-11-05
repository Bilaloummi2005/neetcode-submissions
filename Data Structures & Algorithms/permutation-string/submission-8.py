class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        l = len(s1)
        s1 = sorted(s1)
        while i <= len(s2) - l:
            if sorted(s2[i: i+l]) == s1:
                return True
            i += 1
        return False
        