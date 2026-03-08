import Seq0

print('-----| Exercise 5 |-----')

FOLDER ='sequences/'
GENES = ['U5', 'ADA', 'FRAT1', 'FXN']
bases = ['A', 'C', 'T', 'G']

for gene in GENES:
    filename = FOLDER + gene + '.txt'
    sequence = Seq0.seq_read_fasta(filename)
    count = Seq0.seq_count(sequence)
    print(f'Gene {gene}: {count}')