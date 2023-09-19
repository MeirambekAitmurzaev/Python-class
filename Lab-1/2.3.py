try:
    population = int(input("Enter the population of the universe: "))
    if population % 2 != 0:
        survivors = (population + 1) // 2
    else:
        survivors = population // 2
    print(f"The number of survivors after Thanos snaps his fingers: {survivors}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value for the population.")
