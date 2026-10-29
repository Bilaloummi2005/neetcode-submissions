class Solution:

    def encode(self, strs) -> str:
        l = len(strs)
        out = "".join(strs)
        for s in strs:
            out += ":" + str(len(s))
        out = out + ":" + str(l)
        return out

    def decode(self, s: str):
        meta = s.split(":")
        l = int(meta[-1])
        strs, meta = ":".join(meta[:len(meta)-l-1]), meta[len(meta)-l-1:-1]
        out = []
        i = 0
        for n in meta:
            n = int(n)
            out.append(strs[i: i + n])
            i += n
        return out