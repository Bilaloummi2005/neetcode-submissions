class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        out = False
        i = 0
        s1 = sorted(s1)
        print("s1 = ", s1)
        while i < len(s2) - len(s1) + 1:
            part = s2[i:len(s1)+i]
            print(part)
            if s1 == sorted(part):
                return True
            i+=1
        return out