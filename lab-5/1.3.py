try:    
    frequency_tuples = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]


    list_vow = []
    list_cons = []
    list_symb = []


    def is_vowel(char):
        return char in 'aeiou'


    for symbol, frequency in frequency_tuples:
        if symbol.isalpha():  
            if is_vowel(symbol):
                list_vow.extend([symbol] * frequency)  
            else:
                list_cons.extend([symbol] * frequency)  
        else:
            list_symb.extend([symbol] * frequency)  

    print("List of vowels:", list_vow)
    print("List of consonants:", list_cons)
    print("List of symbols:", list_symb)
except ValueError as e:
        print("Invalid input. Please enter a word.")