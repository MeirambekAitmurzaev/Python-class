try:
    def get_date_in_format(input_date):
        parts = input_date.split('.')
        if len(parts) == 3:
            year, month, day = parts
            return f"{day}.{month}.{year}"
        else:
            return "Invalid date format"


    input_date = "2023.10.23"
    formatted_date = get_date_in_format(input_date)
    print(formatted_date)  
except ValueError as e:
        print("Invalid input.")