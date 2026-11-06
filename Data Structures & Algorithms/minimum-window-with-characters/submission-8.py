class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_bigger(schars, tchars):

            for key, val in tchars.items():
                if val > schars.get(key, 0):
                    return False

            return True
        ls, lt = len(s), len(t)
        if ls < lt:
            return ""
        l = 0

        schars = {}
        tchars = {}


        res, resLen = [0, ls-1], ls+1

        for c in t:
            tchars[c] = tchars.get(c, 0) + 1
            schars[c] = 0
 
        need, have = len(tchars), 0

        for r in range(ls):
            c = s[r]
            if tchars.get(c):
                schars[c] += 1
                if schars[c] == tchars[c]:
                    have += 1
            
            while have == need:
                x = s[l]
                if tchars.get(x):
                    if schars.get(x) >= tchars.get(x):
                        res, resLen = res if res[1] - res[0] < r -l else [l, r], r-l
                        if schars.get(x) == tchars.get(x):
                            have -= 1
                        schars[x] -= 1
                l+=1
        return s[res[0]:res[1]+1] if resLen != ls+1 else ""
























   