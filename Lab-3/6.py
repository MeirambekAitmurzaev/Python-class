try:
    N = int(input("Enter the number of Fibonacci numbers to generate: "))
    
    if N <= 0:
        raise ValueError("N must be a positive integer")
    
    a, b = 0, 1

  
    count = 0


    while count < N:
        print(a, end=" ")  
        a, b = b, a + b  
        count += 1  

except ValueError as e:
    print(f"Error: {e}. Please enter a positive integer for N.")
