try:
    def divide_into_quartiles(list_A):
       
        sorted_list = sorted(list_A)
        
      
        n = len(sorted_list)
        q1_boundary = n // 4
        q2_boundary = 2 * q1_boundary
        q3_boundary = 3 * q1_boundary
        
        
        q1 = sorted_list[:q1_boundary]
        q2 = sorted_list[q1_boundary:q2_boundary]
        q3 = sorted_list[q2_boundary:q3_boundary]
        q4 = sorted_list[q3_boundary:]
        
        
        if n % 4 != 0:
            num_zeros = 4 - (n % 4)
            q1 = [0] * num_zeros + q1
        
        return q1, q2, q3, q4

 
    list_A1 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]
    list_A2 = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4, 8]


    q1_1, q2_1, q3_1, q4_1 = divide_into_quartiles(list_A1)
    q1_2, q2_2, q3_2, q4_2 = divide_into_quartiles(list_A2)


    print("Quartile 1 (q1) - Sample 1:", q1_1)
    print("Quartile 2 (q2) - Sample 1:", q2_1)
    print("Quartile 3 (q3) - Sample 1:", q3_1)
    print("Quartile 4 (q4) - Sample 1:", q4_1)

    print("Quartile 1 (q1) - Sample 2:", q1_2)
    print("Quartile 2 (q2) - Sample 2:", q2_2)
    print("Quartile 3 (q3) - Sample 2:", q3_2)
    print("Quartile 4 (q4) - Sample 2:", q4_2)
except ValueError as e:
        print("Invalid input. Please enter a word.")