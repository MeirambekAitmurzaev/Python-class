try:
    input_list = ['p', 'u', 'l', 'p', ' ', 'f', 'i', 'c', 't', 'i', 'o', 'n']


    symbol_frequency = {}


    for symbol in input_list:
        if symbol in symbol_frequency:
            symbol_frequency[symbol] += 1
        else:
            symbol_frequency[symbol] = 1


    frequency_tuples = [(symbol, frequency) for symbol, frequency in symbol_frequency.items()]

    print("List of tuples with symbol frequencies:")
    print(frequency_tuples)
except ValueError as e:
        print("Invalid input. Please enter a word.")