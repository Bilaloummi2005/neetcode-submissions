class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=False)
        if len(nums) == 0:
            return 0
        # if len(nums) > 500:
        #     return 500
        k = nums[0]
        i = 0
        j = 0
        out = [1]*2
        while i < len(nums)-1:
            print(out)
            if nums[i]+1 == nums[i+1]:
                out[j]+=1   
            else:
                if out[j] > out[(j+1)%2]:
                    j = (j+1)%2
                    out[j] = 1
                else:
                    out[j] = 1
            i+=1
        return max(out)



