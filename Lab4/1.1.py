try:
    user_input = input("Enter a string without whitespaces: ")
    if user_input.isdigit():
        raise ValueError("user_input must be a word not numbers")
    user_tuple = tuple(user_input)
    print("Created tuple is:")
    print(user_tuple)

except ValueError as e:
        print("Invalid input. Please enter a word.")