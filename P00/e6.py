import Seq0

print('-----| Exercise 6 |-----')

FOLDER = "sequences/"
gene = 'U5'
N_bases = 20

filename = FOLDER + gene + '.txt'

sequence = Seq0.seq_read_fasta(filename)

fragment = sequence[:N_bases]
reverse = Seq0.seq_reverse(sequence, N_bases)

print(f'Gene {gene}')
print(f'Fragment: {fragment}')
print(f'Reverse: {reverse}')
