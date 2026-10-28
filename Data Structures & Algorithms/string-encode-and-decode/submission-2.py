class Solution:

    def encode(self, strs) -> str:#time o(m) space o(m+n)
        l = len(strs)#1
        new_str  = ":" + str(l)
        text = ""
        for s in strs:
            new_str = ":" + str(len(s)) + new_str
            text += s
        s = text + new_str
        return s
        

    def decode(self, s: str) :
        strs = s.split(":")
        l = int(strs[-1])
        cuts = strs[len(strs)-l-1: len(strs)-1]#time o(m)
        cuts = cuts[::-1]
        strs = ":".join(strs[:len(strs)-l-1])
        output = []
        o = 0
        for i in cuts:
            i = int(i)
            output.append(strs[o: o+i])
            o += i
        return output