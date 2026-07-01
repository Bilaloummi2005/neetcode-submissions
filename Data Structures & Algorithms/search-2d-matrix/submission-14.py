class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        f, l = 0, len(matrix[0])-1
        F, L = 0, len(matrix)
        i = 0
        while L > F:
            Mid = int(F/2 + L/2)
            print(Mid)
            print(F,L)
            i += 1
            if L == 1:
                break
            if i == 10:
                print("top")
                return 
            if matrix[Mid][f] > target:
                if L == Mid:
                    return False
                L = Mid
            elif matrix[Mid][l] < target:
                if F == Mid:
                    return False
                F = Mid
            else:
                nums = matrix[Mid]
                print(nums)
                i = 0
                while l > f:
                    mid = int(f/2 + l/2)
                    i += 1
                    if i == 10:
                        print("Stop")
                        return True
                    if nums[mid] > target:
                        l = mid - 1
                    elif nums[mid] < target:
                        f = mid + 1
                    elif nums[mid] == target:
                        return True
                    else:
                        return False
                if l == f and nums[f] == target:
                    return True
                return False
        nums = matrix[Mid]
        while l > f:
            mid = int(f/2 + l/2)
            if nums[mid] > target:
                l = mid - 1
            elif nums[mid] < target:
                f = mid + 1
            elif nums[mid] == target:
                return True
            else:
                return False
        if l == f and nums[f] == target:
            return True
        return False