# lines = ["AGTACACTGGT", "ACCAGTGTACT", "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]
# print("From variable: ", lines)

f = open("dna.txt", "r")
lines = f.readlines()
f.close()

print("From file: ", lines)

total_n = 0
bases = {"A:": 0, "C:": 0, "T:": 0, "G:": 0}

for sequence in lines:
    sequence = sequence.strip()
    total_n += len(sequence)

    for base in sequence:
        if base in bases:
            bases[base] += 1
print("Total number of bases: ", total_n)

for base, count in bases.items():
    print(f'¨{base}: {count}')


