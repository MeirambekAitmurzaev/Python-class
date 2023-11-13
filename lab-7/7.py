from collections import Counter
import string

def count_word_frequency(file_path):
    try:
  
        with open(file_path, 'r') as file:

            content = file.read()

    
            content = content.translate(str.maketrans('', '', string.punctuation))


            words = content.split()

 
            word_frequency = Counter(words)

            print("Word Frequency:")
            for word, frequency in word_frequency.items():
                print(f"{word}: {frequency}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_word_frequency("text1.txt")
