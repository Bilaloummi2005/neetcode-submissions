class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = 0
        left = len(matrix)-1
        r = 0
        l = len(matrix[0])-1
        i = 0
        mid = 0
        while len(matrix) > 1 and right <= left:
            mid = (right +left)//2
            if target > matrix[mid][-1]:
                right = mid + 1
            elif target < matrix[mid][0]:
                left = mid - 1
            else:
                break

        while True:
            if r == l-1 or r == l:
                if matrix[mid][r] == target:
                    return True
                if matrix[mid][l] == target:
                    return True
                return False
            midl = (l + r)//2
            if target > matrix[mid][midl]:
                r = midl+1
            elif target < matrix[mid][midl]:
                l = midl-1
            else:
                return True
            i+=1
        return False


# time O(log(n*m))
# space O(1)

