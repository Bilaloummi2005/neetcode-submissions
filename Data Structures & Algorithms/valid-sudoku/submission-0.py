class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_duplicate(board):
            for row in board:
                digits = {str(i):0 for i in range(1,10)}
                for n in row:
                    if n == '.':
                        continue
                    digits[n] += 1
                    if digits[n] > 1:
                        return False
            return True
        i = 0
        columns = []
        while i < 9:
            columns.append([])
            for row in board:
                columns[i].append(row[i])
            i+=1
        squar = [[] for _ in range(9)]
        i = 0
        j = 0
        for j, row in enumerate(board):
            for k, n in enumerate(row):
                i = (j//3)*3 + k //3
                
                squar[i].append(n)
        check = True
        if not check_duplicate(board):
            return False
        if not check_duplicate(columns):
            return False
        if not check_duplicate(squar):
            return False
        return True