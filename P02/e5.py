from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.0.21"
PORT = 8080

c = Client(IP, PORT)

filename = "sequences1/FRAT1.txt"
s = Seq()
s.read_fasta(filename)
gene_seq = str(s)
gene_name = "FRAT1"

start_message = c.talk(f"Sending the {gene_name} Gene to the server, in fragments of 10 bases...")
print(f'Gene{gene_name}:{gene_seq}')

fragments = []
for i in range(5):
    start = i * 10
    fragment = gene_seq[start:start+10]
    fragments.append(fragment)
    print(f'Fragment {i+1}: {fragment}')

for i, fragment in enumerate(fragments, 1):
    response = c.talk(f'Fragment{i}: {fragment}')
    print(response)