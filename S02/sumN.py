# Function for calculating the sum of the N fist integer numbers
def sumn(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print("Sum of the first 20 integer numbers: ", sumn(20))
print("Sum of the first 100 integer numbers: ", sumn(100))