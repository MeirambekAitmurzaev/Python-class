import os

def translate_letter_to_points(letter):
    letter_points = {
        'A+': 4.3, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7
    }
    return letter_points.get(letter, 0.0)

def translate_percentage_to_points(percentage):
    return [4.3 if p >= 95 else
            4.0 if p >= 90 else
            3.7 if p >= 85 else
            3.3 if p >= 80 else
            3.0 if p >= 75 else
            2.7 if p >= 70 else
            2.3 if p >= 65 else
            2.0 if p >= 60 else
            1.7 if p >= 55 else
            1.3 if p >= 50 else
            1.0 if p >= 45 else
            0.7 for p in percentage]

def calculate_gpa(points, credits):
    total_credits = sum(credits.values())  
    if total_credits == 0:
        print("Warning: Total credits are zero. Setting overall GPA to 0.")
        return 0.0
    
    overall_gpa = sum(p * c for p, c in zip(points, credits.values())) / total_credits
    return round(overall_gpa, 2)


def read_grades_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            grades = [line.strip() for line in lines if line.strip()]  
        return grades
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []





def read_credits_file(file_path):
    credits = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    parts = line.strip().split()
                    course = parts[0]
                    credit = int(parts[1])
                    credits[course] = credit
                except (ValueError, IndexError):
                    print(f"Warning: Skipping invalid line in {file_path}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    
    print("Read credits:", credits) 
    return credits


def write_overall_gpas(overall_gpas, output_file_path):
    with open(output_file_path, 'w') as file:
        for course, gpa in overall_gpas:
            file.write(f"{course}: {gpa}\n")

def main():
    directory = "grades"
    credits_file_path = os.path.join(directory, "credits.txt")
    overall_gpas_file_path = os.path.join(directory, "overallGPAs.txt")

   
    if not os.path.exists(directory) or not os.path.exists(credits_file_path):
        print("Error: Directory or files not found.")
        return

    credits = read_credits_file(credits_file_path)

    overall_gpas = []

    for course in ["math", "chemistry", "english"]:
        file_path = os.path.join(directory, f"{course}.txt")
        if not os.path.exists(file_path):
            print(f"Error: File not found - {file_path}")
            continue

        grades = read_grades_file(file_path)
        print("Grades for", course, ":", grades)
        points = [translate_letter_to_points(grade) for grade in grades]
        gpa = calculate_gpa(points, credits)
        overall_gpas.append((course, gpa))

    write_overall_gpas(overall_gpas, overall_gpas_file_path)

if __name__ == "__main__":
    main()
