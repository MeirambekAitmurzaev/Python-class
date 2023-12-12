class Student:
    def __init__(self, name, num_courses, scores):
        self.name = name
        self.num_courses = num_courses
        self.scores = scores
        self.gpa = 0.0
        self.status = ""

    def calculateGPA(self):
        total_points = 0
        total_credits = 0

        for course, details in self.scores.items():
            score = details['score']
            credits = details['credits']
            total_points += score * credits
            total_credits += credits

        if total_credits > 0:
            self.gpa = round(total_points / total_credits, 2)
        else:
            self.gpa = 0.0

    def setStatus(self):
        if self.gpa >= 1.0:
            self.status = "Passed"
        else:
            self.status = "Not Passed"

    def showGPA(self):
        self.calculateGPA()
        print(f"{self.name}'s GPA: {self.gpa}")

    def showStatus(self):
        self.setStatus()
        print(f"{self.name}'s Status: {self.status}")



student_data = {
    'math': {'score': 4.3, 'credits': 4},
    'chemistry': {'score': 3.3, 'credits': 3},
    'english': {'score': 4.0, 'credits': 4}
}

student = Student("John", 3, student_data)


student.showGPA()
student.showStatus()
