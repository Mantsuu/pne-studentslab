
def max_low_temp(temperatures):
    maxi = temperatures[0]
    mini = temperatures[0]
    for t in temperatures:
        if t > mini:
            mini = t
        if t < maxi:
            maxi = t
    return mini, maxi

def temp_average(temperatures):
    if len(temperatures) > 0:
        total = 0
        for num in temperatures:
            total += num
        average = total / len(temperatures)
    return average

def days_above_17_deg(temperatures):
    num_above = 0
    for i in temperatures:
        if i > 17:
            num_above += 1
    return num_above

def list_sorted(temperatures):
    sorted = []
    for i in temperatures:
        if i < temperatures:
            sorted.append(i)
    return sorted

temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

wednesday = temperatures[2]
print("Wedndesday: ", wednesday)

maxim, minim = max_low_temp(temperatures)
print("Max: ", maxim)
print("Min: ", minim)

average_temp = temp_average(temperatures)
print("Average: ", round(average_temp, 1))

days_above = days_above_17_deg(temperatures)
print("Days above 17: ", days_above)

temperatures.sort()
print("Sorted: ", temperatures)