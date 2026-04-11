import socket
from Seq1 import Seq

PORT = 8080
IP = '127.0.0.1'

FOLDER ='sequences2/'
GENES = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']

sequences = [
    'ACCTGGTTTACGTTCTAGGGAGTCGTAGCTAGCTACGTAATAG',
    'CCCCTAGCCCAAAAAAAAAAAATGTCCGAAAAATGGGGGGGGG',
    'AAAAAGCTGATGGGGTTCGGCGCGAGCGGCTCGATGCTTTCCG',
    'GGCTAGAGATTCGCGTTTTTTCGCGATGCGCCCCTGGGGAAAG'
]

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serversocket.bind((IP, PORT))
serversocket.listen()

print('SEQ server configured')
print('Waiting for clients...')

while True:
    client_socket, client_adress = serversocket.accept()
    request = client_socket.recv(2048).decode("utf-8")

    if request == 'PING':
        print('PING command!')
        response = 'OK!'
        print(response)
        client_socket.send(response.encode())
    elif request.startswith('GET'):
        print('GET')
        try:
            index = int(request.split()[1])
            if 0 <= index < len(sequences):
                response = sequences[index] + '\n'
            else:
                response = 'ERROR: Index out of range\n'
        except (IndexError, ValueError):
            response = 'ERROR, invalid format. Use GET <number>\n'
        print(response.strip())
        client_socket.send(response.encode())
    elif request.startswith("INFO"):
        print('INFO')
        try:
            sequence_str = request[5:].strip()
            if not sequence_str:
                response = 'ERROR: no sequence provided'
            else:
                s = Seq(sequence_str)
                response = f'Sequence: {s}'
                response += f'Total length: {s.len()}\n'
                counts = s.count()
                total = s.len()

                for base in ['A', 'T', 'C', 'G']:
                    count = counts[base]
                    if total > 0:
                        percentage = (count/ total * 100)
                    else:
                        percentage = 0
                    response += f'{base}: {count} ({percentage:.3}%\n)'

                print(f'Sequence: {s}')
                print(f'Total length: {s.len()}')
                for base in ['A', 'T', 'C', 'G']:
                    count = counts[base]
                    if total > 0:
                        percentage = (count / total * 100)
                    else:
                        percentage = 0
                    print(f'{base}: {count} ({percentage:.3}%\n)')

        except IndexError:
            response = 'ERROR: invalid format. Use INFO <sequence>\n'
        client_socket.send(response.encode())
    elif request.startswith("COMP"):
        print('COMP')
        try:
            sequence_str = request[5:].strip()
            if not sequence_str:
                response = 'ERROR: no sequence provided'
            else:
                s = Seq(sequence_str)
                complement = s.complement()
                response = complement + '\n'
                print(complement)
        except IndexError:
            response = 'ERROR: invalid format. Use COMP <sequence>\n'
        client_socket.send(response.encode())
    elif request.startswith("REV"):
        print('REV')
        try:
            sequence_str = request[5:].strip()
            if not sequence_str:
                response = 'ERROR: no sequence provided'
            else:
                s = Seq(sequence_str)
                reversed = s.reverse()
                response = reversed + '\n'
                print(reversed)
        except IndexError:
            response = 'ERROR: invalid format. Use REV <sequence>\n'
        client_socket.send(response.encode())
    elif request.startswith("GENE"):
        print('GENE')
        try:
            parts = request.split()
            if len(parts) != 2:
                response = 'ERROR: invalid format. Use GENE <gene_name>\n'
            else:
                gene_name = parts[1]
                if gene_name in GENES:
                    s = Seq()
                    filename = FOLDER + gene_name + '.txt'
                    s.read_fasta(filename)
                    gene_seq = str(s)
                    response = gene_seq  +  '\n'
                    print(f'NULL Seq created')
                    print(gene_seq[:100])
                else:
                    response = f'ERROR: Gene {gene_name} not found.'
        except IndexError:
            response = 'ERROR: invalid format. Use GENE <gene_name>\n'
        client_socket.send(response.encode())
    client_socket.close()