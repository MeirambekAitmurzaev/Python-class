try:
    schoolchildren = int(input("Enter the number of schoolchildren: "))
    total_tangerines = int(input("Enter the total number of tangerines: "))
    tangerines_per_student = total_tangerines // schoolchildren
    remaining_tangerines = total_tangerines % schoolchildren
    print(f"Each student gets {tangerines_per_student} whole tangerines.")
    print(f"{remaining_tangerines} whole tangerines remain in the basket.")
except ValueError:
    print("Invalid input. Please enter valid numerical values for schoolchildren and total tangerines.")
