# You are a Marvel fan and created a list of superheroes.
# avengers  = [‘Iron Man’, ‘Captain America’, ‘Black Widow’, ‘Hulk’, ‘Thor’, ‘Hawkeye’]
# Using this list, calculate how many members in the Avengers team?

avengers  = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']

total_avengers = 1
for avenger in avengers:
    total_avengers += 1
print(f"There are {total_avengers} members in the Avengers team")

# Now Iron Man made Spider-Man a new member of the Avengers, add him to your list at the end

avengers.append("Spider-Man")
# print(avengers)


# Let's add a twist to it. Everyone came to a conclusion that Captain America is the leader of the Avengers, so please add him before the Iron Man.
# Hint: You can first remove him from the list and add before the Iron Man. To remove him you can use a method called .pop()
avengers.remove("Captain America")
avengers.insert(0, "Captain America")
# print(avengers)



# Thor and Hulk are getting angry easily and fight with each other. So you have to separate them with each other.
# To separate them, move “Black Widow” in between them.

avengers.remove("Black Widow")
avengers.insert(3,"Black Widow")
# print(avengers)


# Below list contains scores of students in a class as per their roll number. Which means the first element is for roll # 1, second one is for roll # 2 and so on. Print the scores of,
#
# 1 The first student
# 2 The last student
# 3 First 3 students
# 4 Scores of roll # 3, 4 and 5

scores = [92, 85, 76, 58, 89, 91, 73, 84]

# score of the first student
print(f"First student: {scores[0]}")

# score of the last student
print(f"First student: {scores[-1]}")

# scores of the first 3 students
print(f"First student: {scores[:3]}")

# scores of roll # 3, 4 and 5
print(f"First student: {scores[2:5]}")

# We got a result of one more student which is 83 marks. Append this to the scores at the end and print the list
scores.append(83)
print(scores)

# Categorizes each score into a grade based on the following thresholds:
#
# 1 A: 90 to 100
# 2 B: 80 to 89
# 3 C: 70 to 79
# 4 D: 60 to 69
# 5 F: Below 60
# Count the number of students in each grade category and print the summary of how many students received each grade.
#
# Expected output
#
# Grade Summary:
# - A: 2 students
# - B: 4 students
# - C: 2 students
# - D: 0 students
# - F: 1 students

a_count = b_count = c_count = d_count = f_count = 0
for score in scores:
    if score >= 90:
        a_count += 1
    elif score >= 80:
        b_count += 1
    elif score >= 70:
        c_count += 1
    elif score >= 60:
        d_count += 1
    else:
        f_count += 1

print("Grade Summary")
print(f"- A: {a_count} students")
print(f"- B: {b_count} students")
print(f"- C: {c_count} students")
print(f"- D: {d_count} students")
print(f"- F: {f_count} students")

# Managing inventory efficiently is crucial for businesses to ensure they do not run out of key products. This exercise simulates a simple inventory management system where the user can see which items are below the minimum stock level and need reordering. Below you have two lists that stores product names and their inventory stock levels.Using that,
#
# 1 Check each item to see if its stock level is below a minimum threshold.
# 2 If the stock level is below the minimum, add the product's name to a reorder list.
# 3 Print a list of products that need to be reordered.
#
# Expected Output
#
# Items to Reorder:
# - Pears
# - Grapes

product_names = ["Apples", "Bananas", "Oranges", "Pears", "Grapes"]
stock_levels = [20, 50, 15, 5, 8]

minimum_stock = 10  # Minimum stock before reordering

stock_to_be_reordered = []
for product, stock in zip(product_names, stock_levels):
    if stock < 10:
        stock_to_be_reordered.append(product)

print("\nItems to Reorder")
for product in stock_to_be_reordered:
    print(f"- {product}")