# Define a function to check if a number can be placed in the given position
def is_safe(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Define a function to solve the Sudoku using backtracking
def solve_sudoku(board):
    # Find the next empty space (represented by 0)
    empty = find_empty(board)
    if not empty:
        return True  # Puzzle solved, no empty cells left
    row, col = empty

    # Try every number from 1 to 9
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            # Place the number and attempt to solve the rest
            board[row][col] = num

            # Recursively try to solve the puzzle
            if solve_sudoku(board):
                return True

            # If placing num doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False  # If no number works, return False (backtrack)

# Define a function to find an empty space in the board
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # Return the row, col of the empty cell
    return None

# Function to print the Sudoku grid
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# Main function
def main():
    # Define a Sudoku puzzle (0 represents empty cells)
    board = [
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

    print("Unsolved Sudoku Puzzle:")
    print_board(board)

    # Solve the Sudoku puzzle
    if solve_sudoku(board):
        print("\nSolved Sudoku Puzzle:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
