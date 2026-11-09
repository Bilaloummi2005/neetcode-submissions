class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = 0
        l = len(s)-1
        while r <= l:

            if not s[r].isalnum():
                r += 1
                continue
            if not s[l].isalnum():
                l -= 1
                continue
            if s[l].lower() == s[r].lower():
                l -= 1
                r += 1
            else:
                return False
        return True