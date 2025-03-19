import random
# 1 Generate a random number between 1 and 100
# 2 Asks the user to guess the number
# 3 Provides feedback like "Too high", "Too low correct", or "Correct"
# 4 Keeps track of the number of guesses and displays it when the user guesses correctly
random.seed()
correctNumber = random.randrange(1, 100)

do 
  guess = input("Guess a number between 1-100: ")
while (guess !=)