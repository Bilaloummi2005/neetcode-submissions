class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        out_s = ""
        for s in strs:
            out += ":" + str(len(s))
            out_s += s
        return out_s + out + ":" + str(len(strs))

    def decode(self, s: str) -> List[str]:
        strs = s.split(":")
        l = int(strs[-1])
        count = strs[len(strs)-l-1: len(strs) - 1]
        strs = ":".join(strs[:len(strs)-l-1])
        i = 0
        out = []
        for n in count:
            n = int(n)
            out.append(strs[i:i+n])
            i += n
        return out