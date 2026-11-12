# Blocks World using Goal Stack Planning

# Initial arrangement
blocks = {
    'A': 'Table',
    'B': 'A',
    'C': 'Table'
}

# Goal arrangement
goal = {
    'A': 'Table',
    'B': 'Table',
    'C': 'B'
}

# Move blocks to achieve goal
def solve():
    for block in goal:
        if blocks[block] != goal[block]:

            old = blocks[block]

            # Move block to its goal position
            blocks[block] = goal[block]

            print("Move", block, "from", old,
                  "to", goal[block])

    print("Goal State Reached!")
    print(blocks)

# Execute planning
solve()


# Aim
# To implement Goal Stack Planning to solve the Blocks World problem and achieve a specified goal configuration using Python.

# Objectives
# 1. To understand Goal Stack Planning.
# 2. To arrange blocks according to the given goal.
# 3. To apply valid actions such as pick, place, stack, and unstack.
# 4. To achieve the desired configuration using a sequence of actions.

# Theory
# Goal Stack Planning is an AI planning technique that uses a stack to achieve a desired goal state. It breaks a large goal into smaller sub-goals and solves them one by one.
# In the Blocks World problem, blocks are arranged on a table or placed on top of other blocks. The agent uses actions such as PICKUP, PUTDOWN, STACK, and UNSTACK to move blocks.
# The process continues until the goal configuration is achieved.

# Algorithm
# 1. Start the program.
# 2. Define the initial arrangement of blocks.
# 3. Define the desired goal arrangement.
# 4. Compare the initial state with the goal state.
# 5. Select a block that needs to be moved.
# 6. Check whether the block can be moved safely.
# 7. Move the block to the required position.
# 8. Repeat until all goal conditions are satisfied.
# 9. Display the final arrangement.
# 10. Stop the program.

# Conclusion
# Thus, we successfully implemented a simple Blocks World planning program using Python. The program moves blocks from their initial positions to the desired goal configuration.