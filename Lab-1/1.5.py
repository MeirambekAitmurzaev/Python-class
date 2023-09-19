try:
    edge_length = float(input("Enter the edge length of the cube: "))
    volume = edge_length ** 3
    surface_area = 6 * (edge_length ** 2)
    print(f"Volume of the cube: {volume}")
    print(f"Surface area of the cube: {surface_area}")
except ValueError:
    print("Invalid input. Please enter a valid numerical value for the edge length.")
