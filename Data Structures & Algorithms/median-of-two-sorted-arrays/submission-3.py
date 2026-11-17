class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total//2
        nummin, numbig = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        r = len(nummin)-1
        l = 0
        while True:
            mid = (r+l) //2
            midl = half - mid-2
            nmin = nummin[mid] if mid >= 0 else float("-inf")
            nmin1 = nummin[mid+1] if (mid +1) < len(nummin) else float("inf")
            nbig = numbig[midl] if midl >=0 else float("-inf")
            nbig1 = numbig[midl+1] if (midl + 1) < len(numbig) else float("inf")
            # print(nmin, nmin1, nbig, nbig1)
            if nmin > nbig1:
                r = mid-1
            elif nbig > nmin1:
                l = mid+1
            else:
                # print(nbig, nmin)
                # print(total%2)
                if total % 2:
                    res = min(nbig1, nmin1)
                else:
                    res = (max(nbig, nmin) + min(nbig1, nmin1))/2
                
                break
        return res


# time O(log(min(n, m)))
# space O(1)
