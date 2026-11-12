
# Intelligent Number Guessing Agent

# Hidden number
number = 75

# Set range
low = 1
high = 100

# Guess the number
while low <= high:

    # Calculate middle value
    guess = (low + high) // 2

    print("Agent Guess:", guess)

    # Check the guess
    if guess == number:
        print("Correct Guess!")
        break

    elif guess < number:
        print("Higher")
        low = guess + 1

    else:
        print("Lower")
        high = guess - 1


# Aim
# To design an intelligent agent that guesses a hidden number using higher/lower feedback in Python.

# Objectives
# 1. To understand the working of an intelligent agent.
# 2. To guess a hidden number within a given range.
# 3. To use feedback to improve the next guess.
# 4. To find the correct number using minimum guesses.

# Theory
# A number-guessing intelligent agent is an agent that guesses a hidden number based on feedback received from the environment.
# If the guess is too low, the agent receives "Higher" feedback. If the guess is too high, it receives "Lower" feedback. The agent uses this information to adjust its range and make a better guess.
# This process continues until the correct number is guessed. The agent uses the Binary Search technique to find the number efficiently.

# Algorithm
# 1. Start the program.
# 2. Set the minimum and maximum number.
# 3. Select a hidden number.
# 4. Calculate the middle number as the agent's guess.
# 5. Compare the guess with the hidden number.
# 6. If the guess is correct, display "Correct Guess".
# 7. If the guess is low, increase the minimum value.
# 8. If the guess is high, decrease the maximum value.
# 9. Repeat until the correct number is guessed.
# 10. Stop the program.

# Conclusion
# Thus, we successfully designed an intelligent number-guessing agent using Python. The agent uses higher/lower feedback and the Binary Search technique to find the hidden number efficiently.