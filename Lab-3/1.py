try:
    N = int(input("Enter a positive integer N: "))
    
    if N <= 0:
        raise ValueError("N must be a positive integer")

  
    even_number = 2

   
    while even_number <= N:
        print(even_number)
        even_number += 2  

except ValueError as e:
    print(f"Error: {e}. Please enter a positive integer.")
