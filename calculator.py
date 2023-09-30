from art import logo
from replit import clear

# Defining functions for calculation
def calc(num1,num2,symbol):
  if symbol == '+':
    result = num1+num2
    print(f"num1 + num2 = {result}")
    return result
  elif symbol == '-':
    result = num1-num2
    print(f"num1 - num2 = {result}")
    return result
  elif symbol == '/':
    result = num1/num2
    print(f"num1 / num2 = {result}")
    return result
  else:
    result = num1*num2
    print(f"{num1} * {num2} = {result}")
    return result
  

print(logo)
f_num=float(input("What's your first number? : "))
print("+\n-\n/\n*")
operator = input("Pick an operator: ")
n_num=float(input("What's the next number: "))
value = calc(f_num,n_num,operator)
next_step=input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation : ")
if next_step == 'y':
  while next_step == 'y':
    operator = input("Pick an operator: ")
    n_num=float(input("What's the next number: "))
    value = calc(value,n_num,operator)
    next_step=input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation : ")
  if next_step == 'n':
    clear()
