def count_a_and_b_occurrences(file_path):
    try:
      
        with open(file_path, 'r') as file:

            content = file.read()

    
            count_a = 0
            count_b = 0

      
            for char in content:
                
                if char == 'A' or char == 'a':
                    count_a += 1
                
                elif char == 'B' or char == 'b':
                    count_b += 1

            print(f"A/a occurrences: {count_a}")
            print(f"B/b occurrences: {count_b}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

count_a_and_b_occurrences("text1.txt")
