

def scores(score):
    if 9 <= score <= 10:
        return "A"
    elif 7<= score < 9:
        return "B"
    elif 5<= score < 7:
         return "C"
    elif 2 <= score < 5:
        return "D"
    elif 0 <= score < 3:
        return "F"
    else:
        return "Invalid score"

score = float(input("Enter the score: "))
grades = scores(score)
print(grades)

