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

    
    if submitted_activities >= 4:
        assignment_avg = sum(student.get('assignment', [])) / 4
        lab_avg = sum(student.get('lab', [])) / 2
        test_avg = sum(student.get('test', [])) / 2

        final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
    else:
        final_grade = 0 

   
    student['final_grade'] = final_grade

   
    print(student)
except ValueError as e:
        print("Invalid input. Please enter a word.")