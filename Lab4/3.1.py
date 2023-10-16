try:
    from itertools import groupby

    cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]


    cars_list.sort(key=lambda x: x[0])

    for manufacturer, group in groupby(cars_list, key=lambda x: x[0]):
        group_list = list(group)
        print(f"{manufacturer} {len(group_list)}")
        for car in group_list:
            print(f"- {car[1]}")
except Exception as e:
    print(f"An error occurred: {e}")
