#This is your SRPN file. Make your changes here.

stack = []

# Operator functions


# Addition function, pops the last 2 values from the stack,
# adds them together and then appends the results back to the stack.
def add():
  try:
    num1 = stack.pop()
    num2 = stack.pop()
    result = num1 + num2
  except IndexError:
    print("Stack underflow.")
    stack.append(num2)  #If stack underflow, num2 has to be returned back to the stack.
  else:
    if result > 2147483647:
      stack.append(2147483647)
    elif result < -2147483648:
      stack.append(-2147483648)
    else:
      stack.append(result)


#Equals function, return the value at the top of the stack, if empty print message.
def equals():
  print(stack[-1]) if len(stack) != 0 else print("Stack empty.")


#Subtract function pops the last 2 number on the stack and subtracts them
#in the correct order and appends the result back to the stack.
def subtract():
  try:
    num1 = stack.pop()
    num2 = stack.pop()
    result = num2 - num1
  except IndexError:
    print("Stack underflow.")
    stack.append(num2)
  else:
    if result > 2147483647:
      stack.append(2147483647)
    elif result < -2147483648:
      stack.append(-2147483648)
    else:
      stack.append(result)


#Multiplication function pops the last 2 numbers on the stack and multiplies
#them and appends the result back to the stack.
def multi():
  try:
    num1 = stack.pop()
    num2 = stack.pop()
    result = num1 * num2
  except IndexError:
    print("Stack underflow.")
    stack.append(num2)
  else:
    if result > 2147483647:
      stack.append(2147483647)
    elif result < -2147483648:
      stack.append(-2147483648)
    else:
      stack.append(result)


#Pops 2 numbers and divides them in the correct order.
#If num1 is 0, message printed out and 0 appended.
#Else numbers divided and rounded down.
def div():
  try:
    num1 = stack.pop()
    num2 = stack.pop()
  except IndexError:
    print("Stack underflow.")
    stack.append(num2)
  else:
    if num1 == 0:
      print("Divide by 0.")
      stack.append(int(0))
    elif (num2 == 0):
      stack.append(int(0))
    else:
      if (int(num2 // num1)) > 2147483647:
        stack.append(2147483647)
      elif (int(num2 // num1)) < -2147483648:
        stack.append(-2147483648)
      else:
        stack.append(int((num2 // num1)))


# Pops 2 numbers and gets the remainder in the correct order (rounded down)
def mod():
  try:
    num1 = stack.pop()
    num2 = stack.pop()
  except IndexError:
    print("Stack underflow.")
    stack.append(num2)
  else:
    stack.append(int(num2 % num1))


# Pops 2 numbers and uses the second number as the base
# and the first as its power.
def pow():
  try:
    num1 = stack.pop()
    num2 = stack.pop()
    result = num2**num1
  except IndexError:
    print("Stack underflow.")
    stack.append(num2)
  else:
    if (num1 < 0):
      print("Negative power.")
      stack.append(num2)
      stack.append(num1)
    else:
      if result > 2147483647:
        stack.append(2147483647)
      elif result < -2147483648:
        stack.append(-2147483648)
      else:
        stack.append(result)


#Pushes the number 1804289383 to the stack
def letter_r():
  stack.append(int(1804289383))


#Displays the full stack
def display_stack():
  print(*stack, sep='\n') if len(stack) != 0 else print("-2147483648")


#Checks length of stack and value of interger (put it function)
def check_stack_int():
  command = cmd
  if len(stack) < 23:
    if (int(command) < -2147483648):
      stack.append(-2147483648)
    elif (int(command) > 2147483647):
      stack.append(2147483647)
    elif ((int(command)) == 0):
      stack.append(int(0))
    elif (int(command)):
      stack.append(int(command))
    else:
      print("Unrecognised operator or operand \"" + command + "\"")
  else:
    print("Stack overflow.")


def process_command(command):
  try:
    if (command == "+"):
      add()
    elif (command == "-"):
      subtract()
    elif (command == "*"):
      multi()
    elif (command == "/"):
      div()
    elif (command == "%"):
      mod()
    elif (command == "^"):
      pow()
    elif (command == "r"):
      letter_r()
    elif (command == "d"):
      display_stack()
    elif (command == "="):
      equals()
    else:
      check_stack_int()
  except ValueError:
    print("Unrecognised operator or operand \"" + command + "\"")


#This is the entry point for the program.
#It is suggested that you do not edit the below,
#to ensure your code runs with the marking script
if __name__ == "__main__":
  while True:
    try:
      cmd = input()
      pc = process_command(cmd)
    except EOFError:
      exit()
