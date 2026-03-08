import Seq0

print('-----| Exercise 4 |-----')

FOLDER ='sequences/'
GENES = ['U5', 'ADA', 'FRAT1', 'FXN']
bases = ['A', 'C', 'T', 'G']

for gene in GENES:
    filename = FOLDER + gene + '.txt'
    sequence = Seq0.seq_read_fasta(filename)
    print(f'Gene {gene}:')
    for base in bases:
        count = Seq0.seq_count_base(sequence, base)
        print(f'  {base}: {count}')
