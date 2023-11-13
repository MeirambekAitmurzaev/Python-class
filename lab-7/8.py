import string

def find_longest_word(file_path):
    try:

        with open(file_path, 'r') as file:
       
            content = file.read()

            
            content = content.translate(str.maketrans('', '', string.punctuation))

     
            words = content.split()

        
            longest_word = max(words, key=len)

            print(f"The longest word in the file is: {longest_word}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

find_longest_word("text1.txt")
