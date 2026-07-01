class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        f = []
        l = []
        for num in nums1:
            if num in nums2:
                continue
            else:
                if num in f:
                    continue
                else:
                    f.append(num)
        
        for num in nums2:
            if num in nums1:
                continue
            else:
                if num in l:
                    continue
                else:
                    l.append(num)
            
        return [list(tuple(f)),list(tuple(l))]