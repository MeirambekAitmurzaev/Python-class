try:
    def get_unique_elements_with_count(input_list):
        element_count = {}
        for element in input_list:
         
            element_count[element] = element_count.get(element, 0) + 1
        
        return element_count


    input_list = [1, 2, 3, 1, 2, 4, 1, 2]
    output = get_unique_elements_with_count(input_list)
    print(output) 
except ValueError as e:
        print("Invalid input.")