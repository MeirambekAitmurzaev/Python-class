try:    
    tuple_A = (1, 2, 3, 4, 5, 6, 7)
    tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)

    half_A = len(tuple_A) // 2
    half_B = len(tuple_B) // 2

    result_tuple = tuple_A[:half_A] + tuple_B[half_B:]

    print(result_tuple)
except ValueError:
        print("Invalid input. Please enter a word.")
