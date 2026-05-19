import http.client
import json

GENE_NAME = 'MIR633'
GENE_ID = 'ENSG00000207552'
SERVER = 'rest.ensembl.org'
ENDPOINT = f'/sequence/id/{GENE_ID}'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f'Server: {SERVER}')
print(f'URL: {URL}')

try:
    conn = http.client.HTTPConnection(SERVER)
    conn.request('GET', f'{ENDPOINT + PARAMS}')
    r1 = conn.getresponse()
    print(f'Response received!: {r1.status} {r1.reason}\n')
    if r1.status == 200:
        data1 = r1.read().decode("utf-8")
        response = json.loads(data1)
        print(f'Gene: {GENE_NAME}')
        print(f'Description: {response.get('desc', 'N/A')}')
        print(f'Bases: {response.get('seq', 'N/A')}')
    else:
        print(f'Error: {r1.status} - {r1.reason}')
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
conn.close()