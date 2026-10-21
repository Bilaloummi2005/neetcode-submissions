class Solution:
    def groupAnagrams(self, strs):
        keys = {}
        for i, word in enumerate(strs):
            s_word = "".join(sorted(word))
            if keys.get(s_word):
                keys[s_word].append(word)
            else:
                keys[s_word] = [word]
        return (list(keys.values()))
