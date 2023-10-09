try: 

    user_input = input("Enter a string: ")

    count_of_a = user_input.count('a')

    # Print the result
    print(f"The number of 'a's in the string is: {count_of_a}")
except KeyboardInterrupt:
    print("\nProgram terminated by user.")