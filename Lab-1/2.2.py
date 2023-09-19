try:
    number = int(input("Enter a four-digit number: "))
    thousands_digit = number // 1000
    hundreds_digit = (number % 1000) // 100
    tens_digit = (number % 100) // 10
    units_digit = number % 10
    print(f"The digit in the thousands position is {thousands_digit}")
    print(f"The digit in the hundreds position is {hundreds_digit}")
    print(f"The digit in the tens position is {tens_digit}")
    print(f"The digit in the position of units is {units_digit}")
except ValueError:
    print("Invalid input. Please enter a valid four-digit number.")
