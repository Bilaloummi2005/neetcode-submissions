class Solution:

    def encode(self, strs) -> str:
        l = len(strs)
        new_str  = ":" + str(l)
        text = ""
        for s in strs:
            new_str = ":" + str(len(s)) + new_str
            text += s
        s = text + new_str
        return s
        # print(s)
        # #decode
        # strs = s.split(":")
        # l = int(strs[-1])
        # cuts = strs[len(strs)-l-1: len(strs)-1]
        # strs = ":".join(strs[:len(strs)-l-1])
        # output = []
        # o = 0
        # for i in cuts:
        #     i = int(i)
        #     output.append(strs[o: o+i])
        #     o += i
        # print(output)
        # print(cuts)
        # print(strs)
        

    def decode(self, s: str) :
        strs = s.split(":")
        l = int(strs[-1])
        cuts = strs[len(strs)-l-1: len(strs)-1]
        cuts = cuts[::-1]
        strs = ":".join(strs[:len(strs)-l-1])
        output = []
        o = 0
        for i in cuts:
            i = int(i)
            output.append(strs[o: o+i])
            o += i
        return output