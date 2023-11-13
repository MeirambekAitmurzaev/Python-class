def count_lines_not_starting_with_D(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            lines_not_starting_with_D = sum(1 for line in lines if not line.strip().startswith('D'))

       
            print(f"Number of Lines not starting with 'D': {lines_not_starting_with_D}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


count_lines_not_starting_with_D("text1.txt")
