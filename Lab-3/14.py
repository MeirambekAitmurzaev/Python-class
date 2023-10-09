
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for divisor in range(3, int(num**0.5) + 1, 2):
        if num % divisor == 0:
            return False
    return True


user_input = int(input("Enter a number: "))

while True:
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
        break 
    
  
    user_input += 1
   
