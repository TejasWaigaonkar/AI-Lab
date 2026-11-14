from collections import deque

# 0 = Empty, 1 = Obstacle
grid = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

# Starting and goal positions
start = (0, 0)
goal = (3, 3)

# BFS function
def bfs():

    # Create queue and store starting position
    queue = deque([[start]])

    # Store visited positions
    visited = {start}

    while queue:

        # Remove first path from queue (FIFO)
        path = queue.popleft()

        # Get current position
        x, y = path[-1]

        # Check if goal is reached
        if (x, y) == goal:
            return path

        # Four possible movements: down, up, right, left
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in moves:

            # Calculate new position
            nx = x + dx
            ny = y + dy

            # Check grid boundaries
            if 0 <= nx < 4 and 0 <= ny < 4:

                # Check obstacle and visited position
                if grid[nx][ny] == 0 and (nx, ny) not in visited:

                    # Mark position as visited
                    visited.add((nx, ny))

                    # Add new path to queue
                    queue.append(path + [(nx, ny)])

    # Return None if no path exists
    return None


# Find and display path
path = bfs()

if path:
    print("Path Found:")

    # Display each position in the path
    for position in path:
        print(position)

    # Display total number of moves
    print("Total Moves:", len(path) - 1)

else:
    print("No Path Found!")


# Aim
# To implement Breadth First Search (BFS) to solve a robot path-planning problem in Python using a grid containing obstacles.

# Objectives
# 1. To understand the working of the BFS algorithm.
# 2. To maintain a queue of positions to explore.
# 3. To find a path from the starting position to the goal.
# 4. To identify and avoid obstacles.
# 5. To find the shortest path in an unweighted grid.

# Theory
# Breadth First Search (BFS) is an uninformed search algorithm that explores nodes level by level. It uses a queue (FIFO - First In, First Out) to store positions waiting to be explored.
# In this experiment, the robot navigates a 4x4 grid from the starting position (0,0) to the goal position (3,3). The grid contains empty cells (0) and obstacles (1). BFS explores four possible directions: up, down, left, and right. It maintains a visited set to avoid visiting the same position repeatedly and finds the shortest path to reach the goal.

# Algorithm
# 1. Create a 4x4 grid with empty cells and obstacles.
# 2. Initialize the starting and goal positions.
# 3. Create a queue and add the starting position.
# 4. Mark the starting position as visited.
# 5. Remove the first path from the queue.
# 6. Check whether the goal is reached.
# 7. Explore all four possible directions.
# 8. Add valid and unvisited positions to the queue.
# 9. Repeat until the goal is found or the queue becomes empty.
# 10. Display the shortest path and total moves.

# Conclusion
# Thus, we successfully implemented Breadth First Search (BFS) using Python. The algorithm explores the grid level by level, avoids obstacles, prevents repeated visits, and finds the shortest path from the starting position to the goal.
