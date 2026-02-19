def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter a number: "))
print(f"is_even({number}) = {is_even(number)}")

def classify_triangle(a, b, c):
    if a == b and b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "scalene"

side1= float(input("Enter side 1: "))
side2= float(input("Enter side 2: "))
side3= float(input("Enter side 3: "))

sides = classify_triangle(side1, side2, side3)
print(f"classify_triangle({side1, side2, side3}) = {sides}")