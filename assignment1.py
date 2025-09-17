def make_student(name, scores):
    student = {
        "name": name,
        "scores": scores,
        "average": sum(scores) / len(scores) if scores else 0
    }
    return student

def class_summary(students):
    best_student = None
    highest_average = 0
    for student in students:
        if student["average"] > highest_average:
            highest_average = student["average"]
            best_student = student["name"]
    return best_student

def main():
    gerard=make_student("Gerard", [85, 90, 78]),
    fabrice=make_student("Fabrice", [92, 88, 95]),
    denise=make_student("Denise", [70, 75, 80])
    students = [gerard, fabrice, denise]
    best_student = class_summary(students)
    print(f"The student with the highest average score is: {best_student}")

main()