class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [[] for _ in range(9)]
        rowsSet = {i:{} for i in range(9)}
        boxs = [[] for _ in range(9)]
        boxsSet = {i:{} for i in range(9)}
        for i, r in enumerate(board):
            columnSet = {}
            for j, n in enumerate(r):
                rows[j].append(n)
                idx = ((i//3)*3) + ((j//3))
                boxs[idx].append(n)
                if n == ".":
                    continue
                columnSet[n] = columnSet.get(n, 0) + 1
                rowsSet[j][n] = rowsSet[j].get(n, 0) + 1
                boxsSet[idx][n] = boxsSet[idx].get(n, 0) + 1
                if columnSet.get(n, 0) > 1 or rowsSet[j].get(n, 0) > 1 or boxsSet[idx].get(n, 0) > 1:
                    return False
        return True
board=[ ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]
