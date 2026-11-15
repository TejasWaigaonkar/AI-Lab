# 0 represents an empty cell
board = [
    [1, 0, 0, 4],
    [0, 4, 1, 0],
    [0, 1, 4, 0],
    [4, 0, 0, 1]
]

# Print original Sudoku board
print("Original Sudoku:")
for row in board:
    print(row)

# Check whether a number is valid
def valid(r, c, n):

    # Check the row and column
    for i in range(4):
        if board[r][i] == n or board[i][c] == n:
            return False

    # Check the 2x2 box
    for i in range(2):
        for j in range(2):
            if board[r//2*2+i][c//2*2+j] == n:
                return False

    # Number is valid
    return True


# Solve Sudoku using backtracking
def solve():

    # Check every row and column
    for r in range(4):
        for c in range(4):

            # Find an empty cell
            if board[r][c] == 0:

                # Try numbers from 1 to 4
                for n in range(1, 5):

                    # Check whether number is valid
                    if valid(r, c, n):

                        # Place the number
                        board[r][c] = n

                        # Solve the next empty cell
                        if solve():
                            return True

                        # Backtrack if solution is not found
                        board[r][c] = 0

                # No valid number found
                return False

    # All cells are filled
    return True


# Print solved Sudoku
if solve():
    print("\nSolved Sudoku:")
    for row in board:
        print(row)
else:
    print("No Solution!")


# Aim
# To implement a Sudoku solver using Python and the backtracking technique to solve a 4x4 Sudoku puzzle.

# Objectives
# 1. To understand the working of the backtracking algorithm.
# 2. To identify empty cells in a Sudoku grid.
# 3. To check valid numbers in rows, columns, and 2x2 boxes.
# 4. To fill empty cells with valid numbers from 1 to 4.
# 5. To solve the Sudoku puzzle by applying backtracking.

# Theory
# Sudoku is a number-placement puzzle consisting of a 4x4 grid. The objective is to fill all empty cells with numbers from 1 to 4 without repeating numbers in any row, column, or 2x2 box.
# In this experiment, the backtracking technique is used to solve the Sudoku puzzle. The program finds an empty cell and tries numbers from 1 to 4. It checks whether each number is valid according to Sudoku rules. If a number is valid, it is placed in the cell and the program moves to the next empty cell. If no valid solution is found, the program goes back, removes the previously placed number, and tries another number. This process continues until the puzzle is solved.

# Algorithm
# 1. Create a 4x4 Sudoku grid with empty cells represented by 0.
# 2. Check each row and column to find an empty cell.
# 3. Try numbers from 1 to 4 in the empty cell.
# 4. Check whether the number is valid in its row, column, and 2x2 box.
# 5. If valid, place the number and call the solve function again.
# 6. If the solution fails, reset the cell to 0 (Backtracking).
# 7. Repeat until all cells are filled.
# 8. Display the solved Sudoku or print no solution.

# Conclusion
# Thus, we successfully implemented a Sudoku solver using Python and the backtracking technique. The program checks row, column, and 2x2 box constraints, fills empty cells with valid numbers, and uses backtracking to find the correct solution.
