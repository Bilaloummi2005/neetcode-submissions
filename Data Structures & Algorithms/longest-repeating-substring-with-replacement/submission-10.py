from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = defaultdict(int)
        i = 0
        curr = s[0]
        counter = 0
        diff = 0
        for j, n in enumerate(s):
            my_dict[n] += 1

            maxf = max(my_dict.values())
            while j-i+1 - maxf > k:
                i += 1
                my_dict[curr] -=1
                maxf = max(my_dict.values())
                if i < len(s):
                    curr = s[i]
            counter = max(counter, j - i + 1)
        return counter
        
        