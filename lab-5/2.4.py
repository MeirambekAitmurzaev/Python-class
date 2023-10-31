try:
    student1 = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
    student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}

    
    students = {
        student1['name']: {
            'assignment': student1['assignment'],
            'test': student1['test'],
            'lab': student1['lab'],
            'final_grade': student1['final_grade']
        },
        student2['name']: {
            'assignment': student2['assignment'],
            'test': student2['test'],
            'lab': student2['lab'],
            'final_grade': student2['final_grade']
        }
    }

    
    print(students)
except ValueError as e:
        print("Invalid input. Please enter a word.")