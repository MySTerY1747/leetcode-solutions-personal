# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# Note:
#
#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.


class Solution(object):
    def isValidSudoku(self, board):
        for row in board:
            row_set = set()
            for elm in row:
                if elm.isnumeric():
                    if elm in row_set:
                        return False
                    row_set.add(elm)
        for column_index in range(9):
            column_set = set()
            for elm_index in range(9):
                elm = board[elm_index][column_index]
                if elm.isnumeric():
                    if elm in column_set:
                        return False
                    column_set.add(elm)

        for grid_y_index in range(0, 9, 3):
            for grid_index in range(0, 9, 3):
                grid_set = set()
                grid = []
                for i in range(3):
                    grid.extend(board[grid_y_index + i][grid_index : grid_index + 3])
                for elm in grid:
                    if elm.isnumeric():
                        if elm in grid_set:
                            return False
                        grid_set.add(elm)
        return True


def test_cases():
    cur_solution = Solution()
    try:
        assert (
            cur_solution.isValidSudoku(
                board=[
                    ["5", "3", ".", "9", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
            is True
        )
        assert (
            cur_solution.isValidSudoku(
                board=[
                    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                ]
            )
            is False
        )
    except Exception as e:
        print(f"Test unsuccessful: {e=}")
    else:
        print("All test cases passed.")


if __name__ == "__main__":
    test_cases()
