# Number Guesser. In this game we will be developing a game in which we need to correctly guess the machine random number, in the game there will be help indicadors that will tell the user if the number is High or Low
import random

def get_int(prompt):

  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      valid = True
    except ValueError:
      print("Invalid input - should be an integer.")
  return val

def main():
    print("- Guessing Game -")
    target_number = random.randint(1, 100)
    user_guess = get_int("I’m thinking of a number. Make a guess (1-100):")
    try_count = 0

    while user_guess != target_number:

        if (user_guess <= 0 or user_guess >= 100):
            print("Invalid Input - Should be within range 1-100")
            user_guess = get_int("Guess Again: ")
            try_count += 1

        if user_guess > target_number:
            print("Too high!",end='')
            user_guess = get_int(" Guess Again: ")
            try_count += 1

        if user_guess < target_number:
            print("Too low!",end='')
            user_guess = get_int(" Guess Again: ")
            try_count += 1

    print("Correct! You got it in " + str(try_count) + " trie(s).")


#close def

main()
