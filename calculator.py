def calculate():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            print("Invalid operator.")
            return

        print("Result:", result)
    except ValueError:
        print("Invalid number input.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
