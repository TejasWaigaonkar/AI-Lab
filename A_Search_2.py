
import heapq

# Initial and goal states
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Heuristic: Count misplaced tiles
def h(state):
    return sum(state[i] != goal[i] and state[i] != 0
               for i in range(9))

# Generate possible moves
def neighbors(state):
    result = []
    zero = state.index(0)

    for move in [-3, 3, -1, 1]:
        new = zero + move

        if 0 <= new < 9:
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            temp = list(state)
            temp[zero], temp[new] = temp[new], temp[zero]
            result.append(tuple(temp))

    return result

# A* Search
def astar(start):
    pq = [(h(start), 0, start, [start])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for next_state in neighbors(state):
            if next_state not in visited:
                new_g = g + 1
                new_f = new_g + h(next_state)
                heapq.heappush(pq, (new_f, new_g, next_state,
                                    path + [next_state]))

    return None

# Display solution
path = astar(start)

if path:
    print("Solution Found!")
    for state in path:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
    print("Total Moves:", len(path) - 1)
else:
    print("No Solution Found!")



# Aim
# To implement the A* search algorithm to solve the 8-puzzle problem using Python.

# Objectives
# 1. To understand the A* search algorithm.
# 2. To find the optimal path from the initial state to the goal state.
# 3. To use heuristic functions to guide the search.
# 4. To solve the 8-puzzle problem efficiently.

# Theory
# A* is an informed search algorithm used to find the shortest path to a goal. It uses two values: the actual cost g(n) and heuristic cost h(n).
# The evaluation function is:
# f(n) = g(n) + h(n)
# In the 8-puzzle problem, there are 8 numbered tiles and one empty space. The objective is to arrange the tiles in the correct order by moving tiles into the empty space.

# Algorithm
# 1. Start with the initial puzzle state.
# 2. Define the goal state.
# 3. Calculate the heuristic cost using misplaced tiles.
# 4. Calculate the total cost using f(n) = g(n) + h(n).
# 5. Select the state with the lowest total cost.
# 6. Generate possible states by moving the empty space up, down, left, or right.
# 7. Repeat until the goal state is reached.
# 8. Display the solution path.

# Conclusion
# Thus, we successfully implemented the A* Search algorithm for the 8-puzzle problem using Python. The algorithm uses the heuristic function and path cost to find the optimal solution with minimum moves.
