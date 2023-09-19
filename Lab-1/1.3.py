try:
    
    first_number = int(input("Enter the first number: "))
    second_number = first_number + 1
    third_number = first_number + 2
    print(f"Consecutive Numbers:")
    print(first_number)
    print(second_number)
    print(third_number)
except ValueError:
    print("Invalid input. Please enter a valid integer as the first number.")
