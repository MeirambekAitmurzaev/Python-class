def count_all_and_none_words(file_path):
    try:
        
        with open(file_path, 'r') as file:
            content = file.read()

     
            words = content.split()

            count_all = words.count("all")
            count_none = words.count("none")

            print(f"Occurrences of 'all': {count_all}")
            print(f"Occurrences of 'none': {count_none}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_all_and_none_words("text1.txt")
