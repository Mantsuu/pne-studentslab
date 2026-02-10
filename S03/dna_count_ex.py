
DNA = input("Enter a DNA sequence: ")
print("Total length: ", len(DNA))
bases = (" A:", A, " C:", C, " T:", T, " G:", G)
for base in DNA:
    if base in bases:
        bases[base] += 1
for base, count in bases.items():
    print(f'¨{base}: {count}')

