try:
    
    set_A = {1, 2, 3, 4, 5}
    set_B =  {5,7,8,9,2,10}

    set_A.difference_update(set_B)
    set_B.difference_update(set_A)

    print("Set B after removing elements from set A:", set_B)


except Exception as e:
    print(f"An error occurred: {e}")