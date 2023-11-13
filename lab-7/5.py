def count_words_ending_with_F(file_path):
    try:
   
        with open(file_path, 'r') as file:
         
            content = file.read()

        
            words = content.split()

           
            words_ending_with_F = sum(1 for word in words if word.lower().endswith('f'))

       
            print(f"Number of Words ending with 'F': {words_ending_with_F}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_words_ending_with_F("text1.txt")
