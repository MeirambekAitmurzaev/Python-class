def correct_content(file_path):
    try:
      
        with open(file_path, 'r') as file:
     
            content = file.read()

            content_lower = content.lower()

          
            corrected_content = content_lower.replace('b', 'j')

        
            print("Original Content:")
            print(content)
            print("\nCorrected Content:")
            print(corrected_content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


correct_content("text1.txt")
