try:
    user_input = input("Enter a string with whitespaces: ")
    user_input = user_input.lower()  
    result_list = list(user_input)

    print("Created list is:")
    print(result_list)
except ValueError as e:
        print("Invalid input. Please enter a word.")