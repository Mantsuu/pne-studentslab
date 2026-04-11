from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.0.21"
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

filename = "sequences1/FRAT1.txt"
s = Seq()
s.read_fasta(filename)
gene_seq = str(s)
gene_name = "FRAT1"

start_message1 = c1.talk(f"Sending the {gene_name} Gene to the server, in fragments of 10 bases...")
start_message2 = c2.talk(f"Sending the {gene_name} Gene to the server, in fragments of 10 bases...")

fragments = []
for i in range(10):
    start = i * 10
    fragment = gene_seq[start:start+10]
    fragments.append(fragment)
    print(f'Fragment {i+1}: {fragment}')

print("Sending fragments to servers...")
for i, fragment in enumerate(fragments, 1):
    if i % 2 == 1:
        response = c1.talk(f'Frgament {i}: {fragment}')
    else:
        response = c2.talk(f'Fragment {i}: {fragment}')