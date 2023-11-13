try:  
    def get_words_from_string(input_string):
        words = input_string.split()
        return words

   
    input_string = "This a string with a several words."
    output = get_words_from_string(input_string)
    print(output)  
except ValueError as e:
        print("Invalid input.")