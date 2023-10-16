try:
    import itertools
    import random

    A = {1, 2, 3, 4, 5, 6}
    n = 4
    m = 5


    combinations = list(itertools.combinations(A, n))



    random.shuffle(combinations)

    result = [set(comb) for comb in combinations[:m]]

    print(result)

except Exception as e:
    print(f"An error occurred: {e}")