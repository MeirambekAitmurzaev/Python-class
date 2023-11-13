try:
    def is_prime(number):
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    def get_prime_numbers_in_list(input_list):
        prime_numbers = [num for num in input_list if is_prime(num)]
        return prime_numbers

    
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
    output = get_prime_numbers_in_list(input_list)
    print(output)  
except ValueError as e:
        print("Invalid input.")