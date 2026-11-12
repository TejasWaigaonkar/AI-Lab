
# Sudoku Solver using Backtracking

# 0 represents an empty cell
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

# Check whether number is safe
def valid(r, c, n):
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False

    for i in range(3):
        for j in range(3):
            if board[r//3*3+i][c//3*3+j] == n:
                return False

    return True

# Solve the Sudoku
def solve():
    for r in range(9):
        for c in range(9):

            if board[r][c] == 0:
                for n in range(1, 10):

                    if valid(r, c, n):
                        board[r][c] = n

                        if solve():
                            return True

                        # Backtrack
                        board[r][c] = 0

                return False

    return True

# Print solution
if solve():
    print("Sudoku Solved!")
    for row in board:
        print(row)
else:
    print("No Solution!")



# Aim
# To implement a Sudoku solver using backtracking and constraint propagation techniques in Python.

# Objectives
# 1. To understand the backtracking algorithm.
# 2. To solve a Sudoku puzzle automatically.
# 3. To apply constraints to avoid invalid numbers.
# 4. To find a valid solution for the given Sudoku puzzle.

# Theory
# Sudoku is a number-placement puzzle consisting of a 9×9 grid. The objective is to fill empty cells with numbers from 1 to 9.
# Each row, column, and 3×3 box must contain numbers from 1 to 9 without repetition.
# Backtracking tries possible numbers one by one and goes back whenever a number violates the rules. Constraint propagation checks the possible valid numbers for empty cells and reduces unnecessary choices.

# Algorithm
# 1. Start the program.
# 2. Create a 9×9 Sudoku grid with empty cells represented by 0.
# 3. Find an empty cell in the grid.
# 4. Try numbers from 1 to 9.
# 5. Check whether the number is valid in its row, column, and 3×3 box.
# 6. If valid, place the number in the cell.
# 7. Repeat the process for the next empty cell.
# 8. If no number is valid, remove the previous number and try another number (Backtracking).
# 9. Continue until all cells are filled.
# 10. Display the solved Sudoku and stop.

# Conclusion
# Thus, we successfully implemented a Sudoku solver using Python and the backtracking technique. The program checks the Sudoku constraints, tries valid numbers, and backtracks whenever an invalid choice is made to find the correct solution.