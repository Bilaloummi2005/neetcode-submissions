class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        i = 0
        j = len(s) - 1
        while i <= j:
            while j >= 0 and not s[j].isalnum():
                j -= 1
            while i < len(s) and not s[i].isalnum() :
                i += 1
            if i < len(s) and j >= 0 and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

