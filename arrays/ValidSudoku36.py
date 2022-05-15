import math
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    # step 1: check all rows first ---for duplicates
    total_rows = len(board)
    total_cols = len(board[0])

    hash_row, hash_col = set(), set()
    grid_size = int(math.sqrt(total_rows))
    # hash_box_maps = [dict() for _ in range(total_rows)]
    hash_box_maps = dict()

    for count in range(total_rows * total_cols):

        r = count // total_rows
        c = count % total_cols

        if c == 0:
            hash_row = set()
            hash_col = set()

        # check for duplicates row-wise
        if board[r][c] != ".":
            if board[r][c] in hash_row:
                return False
            else:
                hash_row.add(board[r][c])

        # check for duplicates column-wise
        if board[c][r] != ".":
            if board[c][r] in hash_col:
                return False
            else:
                hash_col.add(board[c][r])

        # for n x n sudoku grid there are n grids of size n/2 * n/2 each.
        # check for duplicates grid-wise using the dict

        if board[r][c] != ".":
            key = str(r // grid_size) + str(c // grid_size)
            if key not in hash_box_maps:
                hash_box_maps.setdefault(key,set())
            if board[r][c] in hash_box_maps[key]:
                return False
            else:
                hash_box_maps[key].add(board[r][c])

    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))

board = [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))

'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'

'''

