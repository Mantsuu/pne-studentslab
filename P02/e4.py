from Client0 import Client
from Seq1 import Seq

FOLDER ="sequences1/"
GENES = ['U5', 'FRAT1', 'ADA']

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


# -- Parameters of the server to talk to
IP = "192.168.0.21" # your IP address
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)
print(c)

for gene in GENES:
    s = Seq()
    filename = FOLDER + gene + '.txt'
    s.read_fasta(filename)

# -- Send a message to the server
print(f"To server: Sending {gene} to the server...")
response = c.talk('Testing!!!')
print(f"Response: {response}")

