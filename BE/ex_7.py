
student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

print(f"Name: {student["name"]}")

print(f"Number of subjects: {len(student["subjects"])}")

print(f"Enrolled in PNE: {"PNE" in student["subjects"]}")

print(f"Databases grade: {student["grades"]["Databases"]}")

grades_list = student["grades"].values()
average = sum(grades_list) / len(grades_list)
print(f"Average grade: {average:.2f}")

print("Subject grades: ")
for subject, grade in student["grades"].items():
    print(f"{subject}: {grade}")
