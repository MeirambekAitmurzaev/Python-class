try:
    from datetime import datetime

    def get_difference_between_dates(date1, date2):
        
        date1_obj = datetime.strptime(date1, '%Y.%m.%d')
        date2_obj = datetime.strptime(date2, '%Y.%m.%d')

        
        date_difference = abs((date2_obj - date1_obj).days)

        return date_difference

    
    date1 = '2023.10.23'
    date2 = '2023.10.24'
    output = get_difference_between_dates(date1, date2)
    print(output)  
except ValueError as e:
        print("Invalid input.")