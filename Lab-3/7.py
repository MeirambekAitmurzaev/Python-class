try: 

    user_input = input("Enter a string: ")

    reversed_string = user_input[::-1]
    print(f"The reversed string is: {reversed_string}")

except KeyboardInterrupt:
    print("\nProgram terminated by user.")