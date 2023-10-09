
user_input = input("Enter a string: ")


user_input = user_input.replace(" ", "").lower()

reversed_input = user_input[::-1]

if user_input == reversed_input:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
