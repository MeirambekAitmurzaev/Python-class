try:
    first_number = int(input("Enter the first number: "))
    seconf_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
    sum=first_number+seconf_number+third_number
    print(f"Sum of the numbers:")
    print(sum)
except ValueError:
    print("Invalid input. Please enter a valid integer as the numbers.")
