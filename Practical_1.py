# Create a grid with Start (S), Goal (G), Empty (0) and Obstacles (X)
grid = [
    ['S', '0', 'X', '0'],
    ['0', '0', 'X', '0'],
    ['X', '0', '0', '0'],
    ['0', '0', '0', 'G']
]

# Set the initial position of the agent
position = [0, 0]

# Store visited positions (Internal State)
visited = set()

# Continue until the goal is reached
while True:
    x, y = position

    # Remember the current position
    visited.add((x, y))

    print("Position:", position)

    # Check if the agent has reached the goal
    if grid[x][y] == 'G':
        print("Goal Reached!")
        break

    # Possible movements: Down, Right, Up, Left
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    moved = False

    # Check all possible movements
    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        # Check grid boundaries, obstacles and visited positions
        if (0 <= nx < 4 and 0 <= ny < 4
            and grid[nx][ny] != 'X'
            and (nx, ny) not in visited):

            # Move the agent to the next valid position
            position = [nx, ny]
            moved = True
            break

    # Stop if no valid movement is available
    if not moved:
        print("No path found!")
        break


# Aim
# To implement a Model-Based Intelligent Agent capable of navigating a grid environment with obstacles using an internal state representation.

# Objectives
# 1. To understand the working of a Model-Based Intelligent Agent.
# 2. To maintain an internal state of the environment.
# 3. To navigate from the starting position to the goal.
# 4. To identify and avoid obstacles.
# 5. To remember previously visited positions and make suitable decisions.

# Theory
# A Model-Based Intelligent Agent is an AI agent that maintains an internal representation of its environment to make decisions. It uses current observations and previously stored information to select suitable actions.
# In this experiment, the agent navigates a 2D grid from a starting point (S) to a goal (G). It avoids obstacles (X) and maintains a record of visited positions to prevent repeated movements. It can move up, down, left, or right until it reaches the goal.

# Algorithm:
# 1. Create a grid containing a starting point (S), goal (G), empty cells (0), and obstacles (X).
# 2. Initialize the agent's position at the starting point.
# 3. Maintain a visited set to store previously visited positions.
# 4. Check all four possible directions (up, down, left, right).
# 5. Move to an unvisited cell that is not an obstacle.
# 6. Repeat until the goal is reached or no valid move is available.

# Conclusion:
# Thus, we successfully implemented a Model-Based Intelligent Agent using Python. The agent maintains an internal state, avoids obstacles, remembers visited positions, and navigates towards the goal.