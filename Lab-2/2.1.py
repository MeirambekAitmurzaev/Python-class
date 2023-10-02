number = input("Enter a four-digit number: ")


if len(number) != 4 or not number.isdigit():
    print("Please enter a valid four-digit number.")
else:
    number = int(number)

    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    ones = number % 10
    
    # Check the condition
    if thousands + ones == abs(tens - hundreds):
        print("yes")
    else:
        print("no")
