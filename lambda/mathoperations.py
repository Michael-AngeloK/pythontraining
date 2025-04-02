square = lambda a: a ** 2

try:
    input = int(input("Enter a number to be squared: "))
    print("The squared number is:", square(input))
except ValueError as a:
    print(f"This input is invalid: {a}")
    