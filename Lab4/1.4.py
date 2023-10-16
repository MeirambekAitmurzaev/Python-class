def count_elements_occurrences(input_tuple):
    element_count = {}
    
    for item in input_tuple:
        if isinstance(item, (list, tuple)):
            item = tuple(item)  
        if item in element_count:
            element_count[item] += 1
        else:
            element_count[item] = 1
    
    result = tuple((key, value) for key, value in element_count.items())
    
    return result

input_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
output_1 = count_elements_occurrences(input_1)
print("Sample Output 1:")
print("Elements and their occurrences:")
print(output_1)


input_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
output_2 = count_elements_occurrences(input_2)
print("\nSample Output 2:")
print("Elements and their occurrences:")
print(output_2)

input_3 = ((1,2,3), (['A', 'B']), (1,2,3), (['A']))
output_3 = count_elements_occurrences(input_3)
print("\nSample Output 3:")
print("Elements and their occurrences:")
print(output_3)
