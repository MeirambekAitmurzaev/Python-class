try:    
    N = int(input("Enter a positive integer N: "))

    if N <= 0:
        raise ValueError("N must be a positive integer")

    
    factorial = 1
    counter = 1

    
    while counter <= N:
        factorial *= counter
        counter += 1

    print(f"The factorial of {N} is {factorial}")


except ValueError as e:
    print(f"Error: {e}. Please enter a positive integer.")
