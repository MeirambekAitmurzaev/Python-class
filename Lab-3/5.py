try: 
    user_input = input("Enter a number: ")
    sum_of_digits = 0

    for char in user_input:
        if char.isdigit():
            digit = int(char)  
            sum_of_digits += digit  
    print(f"The sum of the digits in the number is: {sum_of_digits}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")