try:
    def get_decimal_number_from_binary_string(binary_string):
        decimal_number = int(binary_string, 2)
        return decimal_number

    # Example usage:
    binary_string = "10110011"
    decimal_number = get_decimal_number_from_binary_string(binary_string)
    print(decimal_number)  
except ValueError as e:
        print("Invalid input.")