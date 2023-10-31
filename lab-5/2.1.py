try:
    student_name = "Adam"
    assignment_scores = [82, 56, 44, 30]
    lab_scores = [78.20, 77.20]
    test_scores = [78, 77]

  
    student = {
        'name': student_name,
        'assignment': assignment_scores,
        'lab': lab_scores,
        'test': test_scores
    }

    
    print(student)
except ValueError as e:
        print("Invalid input. Please enter a word.")