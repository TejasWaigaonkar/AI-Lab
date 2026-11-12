
# Tower of Hanoi using State Space Search

# Move disks from one rod to another
def hanoi(n, source, auxiliary, destination):

    # Goal state: No disks left
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    # Move smaller disks to auxiliary rod
    hanoi(n - 1, source, destination, auxiliary)

    # Move largest disk to destination
    print("Move disk", n, "from", source, "to", destination)

    # Move smaller disks to destination
    hanoi(n - 1, auxiliary, source, destination)


# Number of disks
n = 3

# Start the search
hanoi(n, 'A', 'B', 'C')

print("Goal State Reached!")

# Aim
# To implement the Tower of Hanoi problem using State Space Search in Python.

# Objectives
# 1. To understand the concept of State Space Search.
# 2. To move disks from the source rod to the destination rod.
# 3. To follow the rules of Tower of Hanoi.
# 4. To reach the goal state using valid moves.

# Theory
# Tower of Hanoi is a mathematical puzzle consisting of three rods and different-sized disks. The objective is to move all disks from the source rod to the destination rod using an auxiliary rod.
# Only one disk can be moved at a time, and a larger disk cannot be placed on a smaller disk. State Space Search represents each arrangement of disks as a state and finds a sequence of valid moves to reach the goal state.

# Algorithm
# 1. Start the program.
# 2. Initialize the number of disks and three rods (A, B, C).
# 3. Select rod A as the source, B as the auxiliary, and C as the destination.
# 4. If only one disk is present, move it directly to the destination rod.
# 5. Move the top n-1 disks from source to auxiliary rod.
# 6. Move the largest disk from source to destination rod.
# 7. Move the remaining n-1 disks from auxiliary to destination rod.
# 8. Repeat the process until all disks reach the destination rod.
# 9. Display "Goal State Reached!".
# 10. Stop the program.

# Conclusion
# Thus, we successfully implemented the Tower of Hanoi problem using Python. The program moves all disks from the source rod to the destination rod by following the rules and reaching the goal state in the minimum number of moves.