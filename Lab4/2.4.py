try:
    set_A = {1, 2, 3, 4, 7}
    set_B = {8, 7, 9, 4, 2, 0, 10}
    set_C = {4, 0, 1}

    for element in set_A.copy():  
        if element in set_C:
            set_A.remove(element)
            set_B.add(element)


    print("Updated set_C:", set_C.union(set_A))  
except Exception as e:
    print(f"An error occurred: {e}")
