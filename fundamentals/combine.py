# Asks the user to enter a list of numbers (comma-separated).

# Converts the input into a list of integers.

# Uses a loop to find and print the following:

# The largest number in the list.

# The smallest number in the list.

# The sum of all numbers in the list.

# The average of the numbers in the list.

# Challenge: Add error handling to ensure the program doesn't crash if the user enters non-numeric values.

user_input = input("Give me a list of numbers(comma separated): ")

if not user_input:
    raise ValueError("Input cannot be empty")

list = user_input.split(", ")
filtered_list = []

for n in list:
    if n.isnumeric():
        filtered_list.append(n)
       
print(filtered_list)

largest = filtered_list[0]
smallest = filtered_list[0]
sum = 0
average = 0

for n in filtered_list:
    if n > largest:
        largest = n
        
smallest = min(filtered_list)

#Can also use .sort() on the list and take the needed element

for n in filtered_list:
    sum += int(n)

average = int(sum / len(filtered_list))

print("The largest number is: " + largest, "\n The smallest number is: " + smallest, "\n The sum is: " + str(sum), "\n The average is: " + str(average))