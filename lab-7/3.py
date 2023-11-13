def count_uppercase_characters(file_path):
    try:

        with open(file_path, 'r') as file:
            content = file.read()


            uppercase_count = sum(1 for char in content if char.isupper())

            print(f"Number of Uppercase Characters: {uppercase_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_uppercase_characters("text1.txt")
