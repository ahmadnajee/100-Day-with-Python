import random
students = ["Qasem", "Murtaza", "Rahmat", "Ali", "Ahmad"]

students_dict = {student: random.randint(1,100) for student in students}

print(students_dict)

passed_students = { student: score for(student, score) in students_dict.items() if score > 60}
print(passed_students)