sum_of_odd_numbers = 0


while True:
    user_input = input("Enter a number (or 'e' to quit): ")

    if user_input.lower() == 'e':
        break  

    try:
        num = int(user_input) 

        if num % 2 == 0:
            continue
        else:
            sum_of_odd_numbers += num

    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"The sum of odd numbers is: {sum_of_odd_numbers}")
