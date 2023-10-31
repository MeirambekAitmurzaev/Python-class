try:

    student = {
        'name': 'Adam',
        'assignment': [82, 56, 44, 30],
        'lab': [78.2, 77.2],
        'test': [78, 77]
    }

    submitted_activities = 0

    if len(student.get('assignment', [])) == 4:
        submitted_activities += 4
    if len(student.get('lab', [])) == 2:
        submitted_activities += 2
    if len(student.get('test', [])) == 2:
        submitted_activities += 2

    
    submission_check = {
        student['name']: submitted_activities
    }

    
    print(submission_check)
except ValueError as e:
        print("Invalid input. Please enter a word.")
