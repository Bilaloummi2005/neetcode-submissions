class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        best = 0
        searchSet = {}
        foundSet = {}
        for c in s1:
            searchSet[c] = searchSet.get(c, 0) + 1
            # print(l1, r)
        found, need = 0, len(searchSet)
        for r, c in enumerate(s2):
            # print(foundSet, searchSet)
            if r-l >= len(s1):
                k = s2[l]
                if foundSet[k] == searchSet.get(k, 0):
                    found -= 1
                foundSet[k] -= 1
                l += 1
            foundSet[c] = foundSet.get(c, 0) + 1
            if foundSet[c] == searchSet.get(c):
                found += 1
            if found == need:
                return True
        return False
                