import heapq

# Initialize starting and goal states
start = (1,2,3,4,0,6,7,5,8)
goal = (1,2,3,4,5,6,7,8,0)

# Heuristic: Count misplaced tiles (excluding 0)
def heuristic(state):
    return sum(state[i] != goal[i] and state[i] != 0 for i in range(9))

# A* Search function
def astar():

    # Store cost, moves, state and path in priority queue
    queue = [(heuristic(start), 0, start, [start])]

    # Store already visited states
    visited = set()

    while queue:

        # Get state with lowest cost
        cost, moves, state, path = heapq.heappop(queue)

        # Check if goal is reached
        if state == goal:
            print("Solution Found!")

            # Display solution path
            for s in path:
                print(s[:3])
                print(s[3:6])
                print(s[6:])
                print()

            print("Total Moves:", moves)
            return

        # Skip already visited states
        if state in visited:
            continue

        # Mark current state as visited
        visited.add(state)

        # Find position of empty tile (0)
        zero = state.index(0)

        # Four possible movements: up, down, left, right
        for move in [-3, 3, -1, 1]:

            # Calculate new position
            new = zero + move

            # Check grid boundary
            if 0 <= new < 9:

                # Prevent moving left outside the row
                if move == -1 and zero % 3 == 0:
                    continue

                # Prevent moving right outside the row
                if move == 1 and zero % 3 == 2:
                    continue

                # Swap empty tile with adjacent tile
                temp = list(state)
                temp[zero], temp[new] = temp[new], temp[zero]

                # Convert list back to tuple
                new_state = tuple(temp)

                # Check if new state is not visited
                if new_state not in visited:

                    # Calculate actual cost and total cost
                    g = moves + 1
                    f = g + heuristic(new_state)

                    # Add new state to priority queue
                    heapq.heappush(queue, (f, g, new_state, path + [new_state]))

    # If no solution exists
    print("No Solution Found!")


# Call A* Search function
astar()

# Aim
# To implement the A* Search algorithm to solve the 8-puzzle problem using Python with a heuristic function.

# Objectives
# 1. To understand the working of the A* Search algorithm.
# 2. To find a path from the initial state to the goal state.
# 3. To calculate the heuristic cost using misplaced tiles.
# 4. To generate possible puzzle states by moving the empty tile.
# 5. To find the solution with minimum moves.

# Theory
# A* is an informed search algorithm that finds the optimal path using the actual cost and heuristic cost. It uses a priority queue to select the state with the lowest total cost.
# In this experiment, the 8-puzzle consists of 8 numbered tiles and one empty space (0). The objective is to arrange the tiles in the correct order by moving the empty space up, down, left, or right.
# The heuristic function counts the number of misplaced tiles, excluding the empty space. A* uses the formula f(n) = g(n) + h(n), where g(n) is the actual number of moves and h(n) is the estimated cost to reach the goal.

# Algorithm
# 1. Initialize the starting state and goal state.
# 2. Calculate the heuristic cost using misplaced tiles.
# 3. Create a priority queue and add the starting state.
# 4. Select the state with the lowest total cost.
# 5. Check whether the goal state is reached.
# 6. Generate new states by moving the empty tile in four directions.
# 7. Calculate the new cost and add unvisited states to the queue.
# 8. Repeat until the goal is reached or no solution exists.
# 9. Display the solution path and total moves.

# Conclusion
# Thus, we successfully implemented the A* Search algorithm to solve the 8-puzzle problem using Python. The algorithm uses a heuristic function and actual path cost to explore possible states and find an optimal solution with minimum moves.
