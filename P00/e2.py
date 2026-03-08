import Seq0

FOLDER = "sequences/"
FILENAME = "U5.txt"

file_path = FOLDER + FILENAME

sequence = Seq0.seq_read_fasta(file_path)

print(f'DNA file {FILENAME}')
print(f'The first 20 bases are: {sequence[:20]}')