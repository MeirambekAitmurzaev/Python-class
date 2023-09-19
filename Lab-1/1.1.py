try:
    
    input_sequence = input("Enter the sequence of numbers (space-separated): ")
    numbers = [int(num) for num in input_sequence.split()]
    formatted_output = '  '.join(map(str, numbers))
    print(f"Formatted Output: {formatted_output}")
except ValueError:
    print("Invalid input. Please enter a sequence of numbers separated by spaces.")
