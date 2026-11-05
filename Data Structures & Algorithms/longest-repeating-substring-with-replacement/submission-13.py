from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = defaultdict(int)
        i = 0
        counter = 0
        for j, n in enumerate(s):
            my_dict[n] += 1

            maxf = max(my_dict.values())
            while j-i+1 - maxf > k:
                my_dict[s[i]] -=1
                i += 1
                maxf = max(my_dict.values())
            counter = max(counter, j - i + 1)
        return counter
        


# space O(n)
# time O(m)