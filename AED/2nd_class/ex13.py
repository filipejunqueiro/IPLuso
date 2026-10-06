class_grades = {
    "Alex": {12, 20, 15, 9},
    "Peter": {9, 10, 15, 9},
    "Jonny": {12, 12, 15, 9},
    "Timmy": {5, 5, 15, 9},
}

class_grades_avg = {}

for person, grade in class_grades.items():
    avg = sum(grade)/len(grade)
    class_grades_avg.update({person: avg})

for person, avg in class_grades_avg.items():
    if avg > 10:
        print(f"{person} - {avg:.2f}")