

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Set = {}
        s2Set = {}
        i = 0
        l = 0
        while l < len(s1):
            s1Set[s1[l]] = s1Set.get(s1[l], 0) + 1
            s2Set[s2[l]] = s2Set.get(s2[l], 0) + 1
            l += 1
        
        if s1Set == s2Set:
            return True
        while i < len(s2) - l:
            s2Set[s2[i]] -= 1
            if s2Set[s2[i]] == 0:
                s2Set.pop(s2[i])
            s2Set[s2[i + l]] = s2Set.get(s2[i+l], 0) + 1
            i += 1
            if s1Set == s2Set:
                return True
        return False


# time O(n)

# space O(1)




        