class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for c_s, c_t in zip(s, t):
            if not chars.get(c_s):
                chars[c_s] = 1
            else:
                chars[c_s] += 1

            if not chars.get(c_t):
                chars[c_t] = -1
            else:
                chars[c_t] -= 1

        for _, val in chars.items():
            if val == 0:
                pass
            else:
                return False
        return True


# time O(n + m)
# space O(1) if we use only the chars from alphbet dictionary else it O(n)
