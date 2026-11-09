class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            chars = [0]*26
            for c in s:
                chars[ord(c)-ord("a")] += 1
            chars = tuple(chars)
            # print(anagrams)
            if anagrams.get(chars):
                anagrams[chars].append(s)
            else:
                anagrams[chars] = [s]
        return list(anagrams.values())
