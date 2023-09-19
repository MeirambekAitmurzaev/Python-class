try:
   
    input_sequence = input("Enter the sequence of numbers (space-separated): ")
    numbers = [int(num) for num in input_sequence.split()]
    for num in numbers:
            print(num)
except ValueError:
    print("Invalid input. Please enter a sequence of numbers separated by spaces.")
