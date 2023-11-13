import random
def read_and_display_file(file_path):
    try:
        with open(file_path, 'r') as file:

            lines = file.readlines()


            random_line = random.choice(lines)


            print("Random Line:", random_line, end='')
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


read_and_display_file("text1.txt")
