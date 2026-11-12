
from collections import deque

# 0 = Empty, 1 = Obstacle
grid = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

# BFS function
def bfs():
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        x, y = path[-1]

        # Check goal
        if (x, y) == goal:
            return path

        # Four possible movements
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            # Check valid position
            if (0 <= nx < 4 and 0 <= ny < 4
                and grid[nx][ny] == 0
                and (nx, ny) not in visited):

                visited.add((nx, ny))
                queue.append(path + [(nx, ny)])

    return None

# Find and display path
path = bfs()

if path:
    print("Path Found:")
    for position in path:
        print(position)

    print("Total Moves:", len(path) - 1)
else:
    print("No Path Found!")


# Aim
# To implement Breadth First Search (BFS) to solve a robot path-planning problem in Python.

# Objectives
# 1. To understand the BFS algorithm.
# 2. To find a path from the starting point to the goal.
# 3. To avoid obstacles while navigating.
# 4. To find the shortest path in an unweighted grid.

# Theory
# Breadth First Search (BFS) is an uninformed search algorithm that explores nodes level by level. It uses a queue to store nodes waiting to be explored.
# In robot path planning, the environment is represented as a grid containing a starting point, goal, and obstacles. BFS explores all possible movements and finds the shortest path to reach the goal.

# Algorithm
# 1. Start the program.
# 2. Create a grid with a starting point, goal, and obstacles.
# 3. Initialize a queue with the starting position.
# 4. Mark the starting position as visited.
# 5. Remove the first position from the queue.
# 6. Check whether the current position is the goal.
# 7. If not, explore its four neighboring positions.
# 8. Add valid and unvisited positions to the queue.
# 9. Repeat until the goal is found or the queue becomes empty.
# 10. Display the shortest path.
# 11. Stop the program.

# Conclusion
# Thus, we successfully implemented Breadth First Search (BFS) for a robot path-planning problem using Python. The algorithm avoids obstacles and finds the shortest path from the starting position to the goal.