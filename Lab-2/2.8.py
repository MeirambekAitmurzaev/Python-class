weight = int(input())


if weight <= 60:
    category = "Lightweight"
elif weight <= 64:
    category = "First Welterweight"
elif weight <= 69:
    category = "Welterweight"
else:
    category = "Unknown category"

print(category)
