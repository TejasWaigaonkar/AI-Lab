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
# A Model-Based Intelligent Agent is an AI agent that maintains an internal representation of its environment to make intelligent decisions. It uses information about the current environment and its previous states to decide the next action.
# In this experiment, the agent navigates a 2D grid from a starting position [0,0] to a goal position [2,2]. The grid contains obstacles (1) and free paths (0). The agent checks available paths, avoids obstacles, and stores its previously visited positions in an internal state. It moves right whenever possible; otherwise, it tries to move down until it reaches the goal or gets blocked.

# # Algorithm
# 1. Initialize a 3×3 grid with obstacles and free cells.
# 2. Set the agent's starting position and goal position.
# 3. Initialize an empty list to store the agent's internal state.
# 4. Check the right and downward cells for possible movement.
# 5. Move to a free cell and update the internal state.
# 6. Repeat until the goal is reached or the agent gets blocked.
# 7. Display the final position and internal state.

# Conclusion:
# Thus, we successfully implemented a Model-Based Intelligent Agent using Python. The agent maintains an internal state, identifies and avoids obstacles, remembers its previously visited positions, and makes suitable movement decisions to navigate towards the goal.
# Thus, we successfully implemented the A* Search algorithm for the 8-puzzle problem using Python. The algorithm uses the heuristic function and path cost to find the optimal solution with minimum moves.
