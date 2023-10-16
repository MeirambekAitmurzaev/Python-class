try:
    user_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
    user_string = ''.join(user_tuple)
    print("The string is:", user_string)

except ValueError as e:
    print("Invalid input:", e)
