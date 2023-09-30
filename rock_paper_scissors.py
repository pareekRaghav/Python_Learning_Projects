# This is the classic rock, paper, scissors game 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Importing random module
import random 
# Taking user's response
num=int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))

# Printing relevant emoji
if num ==0:
  print(rock)
elif num==1:
  print(paper)
else:
  print(scissors)

# Randomly choosing a option
print("computer's choice:\n")
cchoice =random.randint(0,2)
if cchoice ==0:
  print(rock)
elif cchoice==1:
  print(paper)
else:
  print(scissors)

# Evaluating the winner
if num==0 and cchoice ==0:
  print("its a Draw")
elif num==0 and cchoice==1:
  print("You lose")
elif num==0 and cchoice==1:
  print("You win")
elif num==1 and cchoice==0:
  print("You lose")
elif num==1 and cchoice==1:
  print("its a draw")
elif num==1 and cchoice==2:
  print("You lose")
elif num==2 and cchoice==0:
  print("You lose")
elif num==2 and cchoice==1:
  print("You win")
else:
  print("its a draw")
