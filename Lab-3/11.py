
X = float(input("Enter the base (X): "))
Y = int(input("Enter the exponent (Y): "))


result = 1


while Y > 0:
    result *= X
    Y -= 1


print(f"{X} to the power of {Y} is: {result}")
