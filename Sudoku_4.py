
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

print("Original Sudoku:")
for row in board:
    print(row)

# Check whether a number can be placed safely
def valid(r, c, n):

    # Check the row and column
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False

    # Check the 3x3 box
    for i in range(3):
        for j in range(3):
            if board[r//3*3+i][c//3*3+j] == n:
                return False

    # Number is valid
    return True


# Solve Sudoku using backtracking
def solve():

    # Check every row and column
    for r in range(9):
        for c in range(9):

            # Find an empty cell
            if board[r][c] == 0:

                # Try numbers from 1 to 9
                for n in range(1, 10):

                    # Check whether number is valid
                    if valid(r, c, n):

                        # Place the number
                        board[r][c] = n

                        # Recursively solve next empty cell
                        if solve():
                            return True

                        # Backtrack if solution is not found
                        board[r][c] = 0

                # No valid number found
                return False

    # All cells are filled
    return True


# Print the solved Sudoku
if solve():
    print("\nSudoku Solved!")
    for row in board:
        print(row)
else:
    print("No Solution!")


# Aim
# To implement a Sudoku solver using Python and the backtracking technique to solve a 9x9 Sudoku puzzle.

# Objectives
# 1. To understand the working of the backtracking algorithm.
# 2. To identify empty cells in a Sudoku grid.
# 3. To check valid numbers in rows, columns, and 3x3 boxes.
# 4. To fill empty cells with valid numbers from 1 to 9.
# 5. To solve the Sudoku puzzle by applying backtracking.

# Theory
# Sudoku is a number-placement puzzle consisting of a 9x9 grid. The objective is to fill all empty cells with numbers from 1 to 9 without repeating numbers in any row, column, or 3x3 box.
# In this experiment, the backtracking technique is used to solve the Sudoku puzzle. The program finds an empty cell and tries numbers from 1 to 9. It checks whether each number is valid according to Sudoku rules. If a number is valid, it is placed in the cell and the program moves to the next empty cell. If no valid solution is found, the program goes back, removes the previously placed number, and tries another number. This process continues until the puzzle is solved.

# Algorithm
# 1. Create a 9x9 Sudoku grid with empty cells represented by 0.
# 2. Check each row and column to find an empty cell.
# 3. Try numbers from 1 to 9 in the empty cell.
# 4. Check whether the number is valid in its row, column, and 3x3 box.
# 5. If valid, place the number and call the solve function again.
# 6. If the solution fails, reset the cell to 0 (Backtracking).
# 7. Repeat until all cells are filled.
# 8. Display the solved Sudoku or print no solution.

# Conclusion
# Thus, we successfully implemented a Sudoku solver using Python and the backtracking technique. The program checks row, column, and 3x3 box constraints, fills empty cells with valid numbers, and uses backtracking to find the correct Sudoku solution.
