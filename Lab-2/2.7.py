month = int(input())

if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
elif month == 2:
    days = 28
else:
    print("Invalid month number")
    exit()


print(days)
