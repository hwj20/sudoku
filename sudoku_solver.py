def is_valid(board, row, col, num):
    # Check if the same number exists in the same row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the same number exists in the same column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the same number exists in the 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)

    if not empty_cell:
        return True  # Sudoku puzzle is solved

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Backtrack, try the next number

    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


# Test Sudoku puzzle solver
if __name__ == "__main__":
    # Replace the array below with the Sudoku puzzle you want to solve, use 0 to represent blank cells
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    # sudoku_board = [
    #     [0,0,0,0,0,0,0,0,0],
    #     [2,0,0,0,0,0,0,1,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,0,0,0],
    #     [0,0,0,0,0,0,4,2,1],
    # ]

    if solve_sudoku(sudoku_board):
        for row in sudoku_board:
            print(row)
    else:
        print("This Sudoku puzzle has no solution.")
