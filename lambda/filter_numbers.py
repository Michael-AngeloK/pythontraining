numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda a: a % 2 == 1, numbers))
even_numbers = list(filter(lambda a: a % 2 == 0, numbers))

print("Odd numbers of", numbers, "is this:", odd_numbers)
print("Even numbers of", numbers, "is this:", even_numbers)