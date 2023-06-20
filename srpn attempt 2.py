def srpn_calculator():
    stack = []

    while True:
        input_str = input("Enter the RPN expression: ").split()

        for i in input_str:
            # Check if the input is a number (including octal number)
            if i.isdigit() or (len(i) > 1 and i[0] == '0'):  
                # If it starts with '0', treat it as an octal number
                if i[0] == '0':
                    try:
                        num = int(i, 8)  # Convert octal to decimal
                    except ValueError:
                        print(f"Invalid octal number: {i}")
                        break
                else:
                    num = int(i)
                
                stack.append(num)
                continue

            # Check if the stack has at least two numbers for the operation
            if len(stack) < 2:
                print("Invalid input. Not enough operands.")
                break

            num2 = stack.pop()
            num1 = stack.pop()

            if i == '+':
                result = num1 + num2
            elif i == '-':
                result = num1 - num2
            elif i == '*':
                result = num1 * num2
            elif i == '/':
                if num2 == 0:  # Handle division by zero
                    print("Error: Division by zero.")
                    stack.append(num1)
                    stack.append(num2)
                    break
                result = num1 / num2
            else:
                print(f"Invalid operator: {i}")
                stack.append(num1)
                stack.append(num2)
                break

            stack.append(result)

        if len(stack) == 1:
            print("The result is:", stack.pop())
        else:
            print("Invalid expression or an error occurred.")

srpn_calculator()
