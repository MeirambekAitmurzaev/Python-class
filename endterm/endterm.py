def translateLetter(*letters):
    letter_points = {
        'A+': 4.3, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7
    }
    return [letter_points[letter] for letter in letters]

def translatePercentage(*percentages):
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
            0.7 for p in percentages]

def calculateGPA(*args):
    points = args[::2]  
    credits = args[1::2]  
    overall_gpa = sum(p * c for p, c in zip(points, credits)) / sum(credits)
    return round(overall_gpa, 2)

letters = translateLetter('A+', 'B', 'C')
percentages = translatePercentage(100, 45, 55, 89)
gpa = calculateGPA(3.3, 4, 2.7, 3, 4.0, 4)

print("Translated Letters:", letters)
print("Translated Percentages:", percentages)
print("Overall GPA:", gpa)
