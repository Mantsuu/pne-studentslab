import http.client
import json
import termcolor
from Seq1 import  Seq

genes = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6-269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362'
}
print()
name = input('Write the gene name: ').upper()

if name not in genes:
    print(f'Error: Gene {name} not found')
    print(f'Availabe genes:', '', ''.join(genes.keys()))
    exit()

GENE_ID = genes[name]
SERVER = 'rest.ensembl.org'
ENDPOINT = f'/sequence/id/{GENE_ID}'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f'Server: {SERVER}')
print(f'URL: {URL}')

conn = http.client.HTTPConnection(SERVER)
try:
    conn.request('GET', f'{ENDPOINT + PARAMS}')
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()
print(f'Response received!: {r1.status} {r1.reason}\n')

data1 = r1.read().decode("utf-8")

gene = json.loads(data1)

termcolor.cprint('Gene:', 'green', end='')
print(name)
termcolor.cprint('Description:', 'green', end='')
print(gene['desc'])

genestr = gene['seq']
sequence = Seq(genestr)

total = sequence.len()
print(f'Total length: {total}')

base_counts = sequence.count()
bases = ['A', 'C', 'G', 'T']
for base in bases:
    count = base_counts[base]
    if total > 0:
        percentage = (count/total) * 100
        print(f'{base}: {count} ({percentage:.1f}%)')
    else:
        print(f'{base}: {count} (0,0%)')
most_freq = max(base_counts, key=base_counts.get)
print(f'Most frequent base: {most_freq}')

conn.close()