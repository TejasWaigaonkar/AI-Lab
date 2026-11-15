# Tower of Hanoi using State Space Search (BFS)

# Initial and goal states
start = ((3, 2, 1), (), ())  # All disks are on rod A
goal = ((), (), (3, 2, 1))   # All disks are on rod C

# Queue stores states and paths
queue = [(start, [])]
visited = [start]  # Stores already visited states

# BFS
while queue:

    state, path = queue.pop(0)  # Get the first state from queue

    # Check if goal is reached
    if state == goal:
        print("Goal State Reached!")

        for move in path:
            print(move)

        print("Total Moves:", len(path))
        break

    # Check all possible rod movements
    for i in range(3):
        for j in range(3):

            # Check that source and destination are different
            # and source rod is not empty
            if i != j and state[i]:

                disk = state[i][-1]  # Get the top disk

                # Check if the disk can be moved
                if not state[j] or state[j][-1] > disk:

                    rods = [list(rod) for rod in state]  # Copy rods

                    # Move disk from source to destination
                    rods[i].pop()
                    rods[j].append(disk)

                    # Convert new state into tuple
                    new_state = tuple(tuple(rod) for rod in rods)

                    # Check if state is already visited
                    if new_state not in visited:
                        visited.append(new_state)

                        # Store the movement
                        move = "Move disk " + str(disk) + " from " + "ABC"[i] + " to " + "ABC"[j]

                        # Add new state and path to queue
                        queue.append((new_state, path + [move]))

else:
    print("No Solution!")

# Aim
# To implement the Tower of Hanoi problem using State Space Search (BFS) in Python.

# Objectives
# 1. To understand the concept of State Space Search.
# 2. To represent each arrangement of disks as a state.
# 3. To generate all possible valid movements between rods.
# 4. To use BFS to find the shortest path to the goal state.
# 5. To reach the goal state by following the rules of Tower of Hanoi.

# Theory
# Tower of Hanoi is a mathematical puzzle consisting of three rods and different-sized disks.
# The objective is to move all disks from the source rod to the destination rod.
# Only one disk can be moved at a time, and a larger disk cannot be placed on a smaller disk.
# In State Space Search, each arrangement of disks is considered a state.
# BFS explores these states level by level using a queue and finds the shortest sequence of valid moves.

# Algorithm
# 1. Start the program.
# 2. Initialize the initial state and goal state.
# 3. Create a queue to store states and their paths.
# 4. Create a visited list to avoid checking the same state again.
# 5. Remove the first state from the queue.
# 6. Check whether the current state matches the goal state.
# 7. Generate all possible valid disk movements between the three rods.
# 8. Create a new state after each valid movement.
# 9. Add unvisited states to the queue.
# 10. Repeat until the goal state is reached.
# 11. Display the solution and total number of moves.
# 12. Stop the program.

# Conclusion
# Thus, we successfully implemented the Tower of Hanoi problem using State Space Search (BFS) in Python.
# The program explores different states and finds the shortest sequence of valid moves to reach the goal state.
