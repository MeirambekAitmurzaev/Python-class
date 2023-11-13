try:
    def get_elements_with_no_more_than_two_occurrences(input_list):
        result = []
        seen = set()
        
        for element in input_list:
                
                if input_list.count(element) >= 2 and element not in seen:
                    result.append(element)
                    seen.add(element)
        
        return result


    input_list = [1, 2, 3, 1, 2, 4]
    output = get_elements_with_no_more_than_two_occurrences(input_list)
    print(output)  
except ValueError as e:
        print("Invalid input.")