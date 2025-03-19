from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_list = []
        for _ in range(9):
            rows_list.append(set())
        columns_list = []
        for _ in range(9):
            columns_list.append(set())

        grid_map = {}
        for i in range(3):
            for j in range(3):
                grid_map[(i, j)] = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if (num == ".") :
                    continue
                
                if (num in rows_list[i]):
                    return False
                else:
                    rows_list[i].add(num)
                
                if (num in columns_list[j]):
                    return False
                else: 
                    columns_list[j].add(num)

                box_index = (i//3, j//3)
                if num in grid_map[box_index]:
                    return False  
                grid_map[box_index].add(num)
        return True

    
solution = Solution()
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board1))  # Expected: True

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board2))  # Expected: False

board3 = [
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]
 ]

print(solution.isValidSudoku(board3)) # Expected False