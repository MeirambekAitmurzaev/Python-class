try:
    def get_keys_with_value_true(input_dict):
        result = [key for key, value in input_dict.items() if value is True]
        return result

    my_dict = {
        "a": True,
        "b": False,
        "c": True,
    }

    result = get_keys_with_value_true(my_dict)
    print(result) 
except ValueError as e:
        print("Invalid input.")