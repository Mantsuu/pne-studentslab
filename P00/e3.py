import Seq0

FOLDER ='sequences/'
GENES = ['U5', 'ADA', 'FRAT1', 'FXN']

print('-----| Exercise 3 |-----')

for gene in GENES:
    filename = FOLDER + gene + '.txt'
    sequence = Seq0.seq_read_fasta(filename)
    length = Seq0.seq_len(sequence)
    print(f'Gene {gene} -> Length: {length}')