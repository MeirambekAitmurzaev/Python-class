try:
    def is_perfect_square(n):
        sqrt_n = int(n ** 0.5)
        return sqrt_n * sqrt_n == n

    def are_all_perfect_squares(numbers):
        return all(is_perfect_square(num) for num in numbers)

    
    numbers = [4, 25, 81]
    result = are_all_perfect_squares(numbers)
    print(result) 
except ValueError as e:
        print("Invalid input.")