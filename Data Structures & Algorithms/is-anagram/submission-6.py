class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        chars = {}
        for s_char, t_char in zip(s, t):
            if chars.get(s_char):
                chars[s_char] -= 1
            else:
                chars[s_char] = -1
            if chars.get(t_char):
                chars[t_char] += 1
            else:
                chars[t_char] = 1
        for val in chars.values():
            if val != 0:
                return False
        return True
        
        