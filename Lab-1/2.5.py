try:
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))

    operation = input("Please choose the operation (+, -, *, /): ")


    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number == 0:
            print("Division by zero is not allowed.")
            result = None
        else:
            result = first_number / second_number
    else:
        print("Invalid operation. Please choose one of '+', '-', '*', or '/'")
        result = None

    if result is not None:
        print(f"{first_number} {operation} {second_number} = {result}")

except ValueError:
    print("Invalid input. Please enter valid numerical values.")
