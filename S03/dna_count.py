def count_DNA(letter):
    count = 0
    c_A = 0
    c_C = 0
    c_T = 0
    c_G = 0
    while count < len(letter):
        if letter[count] == "A":
            c_A += 1
        elif letter[count] == "C":
            c_C += 1
        elif letter[count] == "T":
            c_T += 1
        elif letter[count] == "G":
            c_G += 1
        count += 1
    return c_A, c_C, c_T, c_G
DNA = input("Enter a DNA sequence: ")
print("Total length: ", len(DNA))
A, C, T, G = count_DNA(DNA)
print(" A:", A, " C:", C, " T:", T, " G:", G)

