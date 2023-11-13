try:
    def get_prime_numbers(n):
       
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False 
        
  
        p = 2
        
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1

        
        prime_numbers = [i for i in range(2, n + 1) if is_prime[i]]
        
        return prime_numbers

    n = 100
    output = get_prime_numbers(n)
    print(output)
except ValueError as e:
        print("Invalid input.")