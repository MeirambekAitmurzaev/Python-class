try:
    population = int(input("Enter the population of the universe: "))
    if population != 0:
        survivors = population+1
        print(f"The result of << is: {survivors}")
    else:
        print(f"it is 0")
except ValueError:
    print("Invalid input. Please enter a valid numerical value for the population.")
