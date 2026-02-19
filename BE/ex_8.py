
students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

def average(grades):
    return sum(grades) / len(grades)

def get_status(avg):
    if avg >= 5:
        return "PASS"
    else:
        return "FAIL"

pass_count = 0
fail_count = 0

for student in students:
    name = student["name"]
    grades = student["grades"]

    avg = average(grades)
    status = get_status(avg)

    if status == "PASS":
        pass_count += 1
    else:
        fail_count += 1

    print(f"{name}: {avg:.1f} -> {status} ")
print(f"Results: {pass_count} passed, {fail_count} failed ")