# To implement Goal Stack Planning for Blocks World

# Initial arrangement of blocks
blocks = {
    'A': 'table',
    'B': 'A',
    'C': 'table'
}

# Goals to be achieved
goal_stack = [
    ('C', 'B'),
    ('B', 'table'),
    ('A', 'table')
]

# Check whether a block is clear
def clear(block):
    return all(position != block for position in blocks.values())


# Function to solve the problem
def solve():

    # Continue until all goals are checked
    while goal_stack:

        # Get the next goal from the stack
        block, destination = goal_stack.pop()

        # Skip if the block is already in the correct position
        if blocks[block] == destination:
            continue

        # Check whether the block and destination are clear
        if clear(block) and (destination == 'table' or clear(destination)):

            # Store the old position
            old = blocks[block]

            # Move the block to its destination
            blocks[block] = destination

            # Display the movement
            print("Moved", block, "from", old, "to", destination)

    # Check whether the goal state is achieved
    if blocks == {'A': 'table', 'B': 'table', 'C': 'B'}:
        print("Goal State Reached!")
    else:
        print("Goal State Not Reached!")

    # Display the final arrangement
    print("Final State:", blocks)


# Execute the program
solve()

# Aim
# To implement Goal Stack Planning for the Blocks World problem using Python.

# Objectives
# 1. To understand Goal Stack Planning.
# 2. To arrange blocks in the required positions.
# 3. To check whether blocks can be moved safely.
# 4. To achieve the goal state.

# Theory
# Goal Stack Planning is an AI technique that uses a stack to achieve a goal.
# In Blocks World, blocks are moved from one position to another.
# The program checks block positions and performs valid movements
# until the required arrangement is achieved.

# Algorithm
# 1. Start the program.
# 2. Define the initial block arrangement.
# 3. Define the goal stack.
# 4. Check whether a block is clear.
# 5. Move the block if the movement is valid.
# 6. Repeat until all goals are checked.
# 7. Display the final state.
# 8. Stop the program.

# Conclusion
# Thus, we successfully implemented Goal Stack Planning
# to arrange blocks according to the given goal state using Python.
