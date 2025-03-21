# Asks the user to enter a list of numbers (comma-separated).

# Converts the input into a list of integers.

# Uses a loop to find and print the following:

# The largest number in the list.

# The smallest number in the list.

# The sum of all numbers in the list.

# The average of the numbers in the list.

# Challenge: Add error handling to ensure the program doesn't crash if the user enters non-numeric values.

try:
    user_input = input("Give me a list of numbers(comma separated): ")
    if not user_input:
        raise ValueError("Input cannot be empty")

    num_list = [int(n) for n in user_input.split(",")]

    largest = max(num_list)
    smallest = min(num_list)
    total_sum = sum(num_list)
    average = total_sum / len(num_list)

    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")
    print(f"The sum is: {total_sum}")
    print(f"The average is: {average}")

except ValueError as e:
    print(f"Invalid input: {e}")