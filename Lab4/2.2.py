try:
    set_A = {1, 2, 3, 4, 5}
    set_B = {5, 7, 8, 9, 2, 10}


    difference_A_B = set_A - set_B
    difference_B_A = set_B - set_A


    result_set = difference_A_B.union(difference_B_A)


    print(result_set)
except Exception as e:
    print(f"An error occurred: {e}")