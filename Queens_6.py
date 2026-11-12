
# 8 Queens using Backtracking

N = 8

# Create an empty chessboard
board = [[0 for i in range(N)] for j in range(N)]

# Check whether position is safe
def safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

        if col - (row-i) >= 0 and board[i][col-(row-i)] == 1:
            return False

        if col + (row-i) < N and board[i][col+(row-i)] == 1:
            return False

    return True

# Solve using backtracking
def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Display solution
if solve(0):
    print("Solution Found!")
    for row in board:
        print(row)
else:
    print("No Solution Found!")


# Aim
# To implement Backtracking Search to solve the 8-Queens Constraint Satisfaction Problem using Python.

# Objectives
# 1. To understand the backtracking search algorithm.
# 2. To place 8 queens on a chessboard.
# 3. To ensure that no two queens attack each other.
# 4. To find a valid solution using constraints.

# Theory
# The 8-Queens problem is a chess puzzle in which 8 queens must be placed on an 8×8 chessboard so that no two queens attack each other.
# No two queens should be in the same row, column, or diagonal. Backtracking tries different positions and removes a queen whenever a constraint is violated. It continues until a valid arrangement is found.

# Algorithm
# 1. Start the program.
# 2. Create an 8×8 chessboard.
# 3. Place a queen in the first row.
# 4. Check whether the position is safe.
# 5. If safe, place the queen and move to the next row.
# 6. Repeat until all 8 queens are placed.
# 7. If no safe position is available, remove the previously placed queen and try another position.
# 8. Display the solution when all queens are placed.
# 9. Stop the program.

# Conclusion
# Thus, we successfully implemented the 8-Queens problem using Backtracking Search in Python. The program places 8 queens on the chessboard while satisfying all constraints and ensuring that no two queens attack each other.