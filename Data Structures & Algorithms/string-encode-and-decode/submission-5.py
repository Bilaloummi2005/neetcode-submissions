class Solution:

    def encode(self, strs: [str]) -> str:
        l = len(strs)
        out =""
        out_s = ""
        for s in strs:
            out += ":" + str(len(s))
            out_s += s
        return out_s + out + ":" + str(l)

    def decode(self, s: str) -> [str]:
        strs = s.split(":")
        l = int(strs[-1])
        chunks = strs[len(strs) - l - 1: len(strs) - 1]
        strs = ":".join(strs[:len(strs)-l-1])
        out = []
        pre = 0
        for n in chunks:
            n = int(n)
            print(n)
            out.append(strs[pre: pre+n])
            pre += n
        return (out) 
