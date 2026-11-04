class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        outs = ""
        for s in strs:
            out += ":" + str(len(s))
            outs+= s
        return outs + out+":" + str(len(strs))

    def decode(self, s: str) -> List[str]:
        strs = s.split(":")
        l = int(strs[-1])
        cut = strs[len(strs)-l-1: len(strs)-1]
        strs = ":".join(strs[:len(strs)-l-1])
        print(strs)
        print(cut)
        print(l)
        out = []
        i = 0
        for n in cut:
            n = int(n)
            out.append(strs[i:i+n])
            i+=n
        return out