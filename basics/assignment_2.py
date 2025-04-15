
avengers  = ['Iron Man', 'Captain America', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']

total_avengers = 1
for avenger in avengers:
    total_avengers += 1
print(f"There are {total_avengers} members in the Avengers team")


avengers.append("Spider-Man")
# print(avengers)


avengers.remove("Captain America")
avengers.insert(0, "Captain America")
# print(avengers)



avengers.remove("Black Widow")
avengers.insert(3,"Black Widow")
# print(avengers)


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