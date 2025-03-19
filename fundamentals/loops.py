import random
# 1 Generate a random number between 1 and 100
# 2 Asks the user to guess the number
# 3 Provides feedback like "Too high", "Too low correct", or "Correct"
# 4 Keeps track of the number of guesses and displays it when the user guesses correctly
random.seed()
correctNumber = random.randrange(1, 100)
lowest = 1
highest = 100
guess = 0
counter = 0

while True:
  guess = int(input("Guess a number between 1-100: "))
  counter += 1
  if guess < lowest or guess > highest:
    print(f"Please enter a number between {lowest} and {highest}.")
    continue
  if guess < correctNumber:
    print("Too low!")
  elif guess > correctNumber:
    print("Too high!")
  else:
    print(f"Correct! You guessed the number in {counter} tries.")
    break