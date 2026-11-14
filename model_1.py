grid = [
    [0,0,0],
    [1,1,0],
    [0,0,0]
]

agent = [0,0]
goal = [2,2]
internal_state = []
print("agent start at:",agent)

while agent != goal:
    internal_state.append(agent.copy())

    row = agent[0]
    col = agent[1]

    if col+1<3 and grid[row][col+1] == 0:
        agent[1] = agent[1]+1

    elif row+1<3 and grid[row+1][col] == 0:
        agent[0]=agent[0]+1

    else:
        print("agent is blocked",agent)
        break
    print("agent moved to",agent)

if agent == goal:
    print("agent reached goal",agent)
print("internal state",internal_state)


# Aim
# To implement a Model-Based Intelligent Agent capable of navigating a 3x3 grid environment with obstacles using an internal state representation.

# Objectives
# 1. To understand the working of a Model-Based Intelligent Agent.
# 2. To maintain an internal state of the environment.
# 3. To navigate from the starting position to the goal.
# 4. To identify and avoid obstacles.
# 5. To remember previously visited positions and make suitable decisions.

# Theory
# A Model-Based Intelligent Agent is an AI agent that maintains an internal representation of its environment to make decisions. It uses current observations and previously stored information to select suitable actions.
# In this experiment, the agent navigates a 2D grid from a starting position [0,0] to a goal position [2,2]. It avoids obstacles (represented by 1) and moves through empty cells (represented by 0). The agent maintains an internal state to store its previously visited positions. It first tries to move right and then down if the right path is blocked.

# Algorithm:
# 1. Create a 3x3 grid containing empty cells (0) and obstacles (1).
# 2. Initialize the agent's position at [0,0].
# 3. Set the goal position to [2,2].
# 4. Initialize an empty list to maintain the internal state.
# 5. Store the current agent position in the internal state.
# 6. Check whether the right cell is within the grid and is not an obstacle.
# 7. If the right cell is free, move the agent right.
# 8. Otherwise, check whether the bottom cell is within the grid and is not an obstacle.
# 9. If the bottom cell is free, move the agent down.
# 10. If both directions are blocked, stop the agent.
# 11. Repeat until the agent reaches the goal or gets blocked.
# 12. Display the final position and internal state.

# Conclusion:
# Thus, we successfully implemented a Model-Based Intelligent Agent using Python. The agent maintains an internal state, identifies and avoids obstacles, remembers its previously visited positions, and makes suitable movement decisions to navigate towards the goal.
# Thus, we successfully implemented the A* Search algorithm for the 8-puzzle problem using Python. The algorithm uses the heuristic function and path cost to find the optimal solution with minimum moves.
