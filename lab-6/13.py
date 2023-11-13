try:
    def get_words_starting_with_vowel(words):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_words = [word for word in words if word[0].lower() in vowels]
        return vowel_words

    
    words = ["apple", "banana", "orange", "bear", "cat"]
    vowel_starting_words = get_words_starting_with_vowel(words)
    print(vowel_starting_words)
except ValueError as e:
        print("Invalid input.")