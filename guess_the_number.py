# In this game the computer randomly selects a number between 1 and 100 and the user has to identify that number by guessing numbers. 
# As the user guesses a number the computer tells whether he is close to the number or far away and accordingly the user can guess the next number. 
# But the user gets limited number of attempts based on the difficulty level he/she chooses.

import random
def game():
  choice = random.randint(1,100)
  print("Welcome to the number guessing game.")
  print("I am thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty level. Type 'easy' or 'hard' : ")
  
  if difficulty == 'easy':
    attempts = 10
  else:
    attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number")
  
  while attempts>0:
    guess = int(input("Make a guess: "))
    if guess > choice:
      attempts-=1
      print(f"Too high.\nGuess Again.\nYou have {attempts} attempts remaining to guess the number ")
    elif guess<choice:
      attempts-=1
      print(f"Too low.\nGuess Again.\nYou have {attempts} attempts remaining to guess the number")
    elif guess == choice:
      attempts=0
      print(f"You got it. The answer is {choice}")
  again = input("Wanna play it again? Type 'y' for yes and 'n' for no.")
  if again == 'y':
    game()

# Calling the game function
game()
  

  
