try:  
    user_input =input("Enter a string without whitespaces: ")
    if user_input.isdigit():
                raise ValueError("user_input must be a word not numbers")


    input_set = set(user_input.replace(" ", ""))


    print("Created set is:")
    print(input_set)

except ValueError:
        print("Invalid input. Please enter a word.")
