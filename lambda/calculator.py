def add(i, j):
    return i + j

def subtract(i, j):
    return i - j

def multiply(i, j):
    return i * j

def divide(i, j):
    if j == 0:
        raise ValueError("Division by zero is not allowed.")
    return i / j

while True:
    print("\nCalculator")
    print("1. Add {first_number, second_number} ")
    print("2. Subtract {first_number, second_number} ")
    print("3. Multiply {first_number, second_number} ")
    print("4. Divide {first_number, second_number} ")
    print("Type 'exit' to quit.")

    try:
        choice = input("\nWrite down the operation with the variable numbers here: ").strip()
        
        if choice.lower() == "exit":
            print("Exiting... Goodbye!")
            break
        
        parts = choice.split()
        if len(parts) != 3:
            print("Input must be within the format: operation number1 number2")
            continue
        
        operation, number_1, number_2 = parts[0], parts[1], parts[2]
        number_1, number_2 = float(number_1), float(number_2)

        if operation == "1" or operation.lower() == "add":
            result = add(number_1, number_2)
        elif operation == "2" or operation.lower() == "subtract":
            result = subtract(number_1, number_2)
        elif operation == "3" or operation.lower() == "multiply":
            result = multiply(number_1, number_2)
        elif operation == "4" or operation.lower() == "divide":
            result = divide(number_1, number_2)
        else:
            print("Invalid operation. Please choose 1, 2, 3, or 4.")
            continue
            
        print(f"The result is = {result}")
        
    except ValueError as e:
        print(f"Invalid input: {e}")
