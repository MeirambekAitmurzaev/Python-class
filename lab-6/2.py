try:
    def get_unique_elements(input_list):
        result = []
        seen = set()
        for item in input_list:
            if input_list.count(item) == 1 and item not in seen:
                result.append(item)
                seen.add(item)
        return result

    my_list = [1, 2, 3, 1, 2, 4]
    result = get_unique_elements(my_list)
    print(result)  
except ValueError as e:
        print("Invalid input.")