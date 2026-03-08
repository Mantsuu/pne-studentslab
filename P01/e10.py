from Seq1 import Seq

print('----| Practice 1, Exercise 10 |----')

FOLDER ='sequences1/'
GENES = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
bases = ['A', 'C', 'T', 'G']

for gene in GENES:
    s = Seq()
    filename = FOLDER + gene + '.txt'
    s.read_fasta(filename)
    count = s.count()
    most_frequent = max(count, key=count.get)
    print(f'Gene {gene}: Most frequent Base: {most_frequent}')
