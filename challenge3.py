# create a grade analyzer for a coding bootcamp

student_grades = [("Faith", 97.3), ("Kate", 92.6), ("Mercy",90.7) ]

def grade_analyzer(student_grades,operation):

    grades = []

    for student in student_grades:
        grades.append(student [1])

    if operation == "average":
        average = sum(grades)/len(student_grades)   
        return average

    elif operation == "highest":
        highest = grades[0]
        for grade in grades:
            if grade > highest:
                highest = grade
        return highest

    elif operation == "lowest":
        lowest = grades [0]
        for grade in grades:
            if grade < lowest:
                lowest = grade
        return lowest

print(grade_analyzer(student_grades, "lowest"))

