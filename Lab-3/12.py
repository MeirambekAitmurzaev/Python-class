N = int(input("Enter a positive integer N: "))

print("Prime numbers in the range from 1 to", N, "are:")

num = 2

while num <= N:
    is_prime = True  


    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False  
            break  
        divisor += 1

    if is_prime:
        print(num, end=" ")

    num += 1

print()  
