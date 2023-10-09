try:
    while True:
        user_input = input("Enter a number: ")
        try:
            num = int(user_input)
        except ValueError:
            print("Error: Please enter a valid integer.")
            continue  
        
        if num == 42:
            print("You found the magic number (42)! Exiting the program.")
            break
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
