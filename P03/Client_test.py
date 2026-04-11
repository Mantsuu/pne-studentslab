from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

PORT = 8080
IP = '127.0.0.1'

c = Client(IP, PORT)
print(c)

print('Testing PING...')
response = c.talk('PING')
print(response)

print('Testing GET...')
for i in range(5):
    response = c.talk(f'GET {i}')
    print(f'GEt {i}: {response}')

seq_get0 = c.talk('GET 0').strip()

print('Testing INFO...')
response = c.talk(f'INFO {seq_get0}')
print(response)

print('Testing COMP...')
print(f'COMP: {seq_get0}')
response = c.talk(f'COMP {seq_get0}')
print(response)

print('Testing REV...')
print(f'REV: {seq_get0}')
response = c.talk(f'REV {seq_get0}')
print(response)

print('Testing GENE...')
GENES = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']
for gene in GENES:
    response = c.talk(f'GENE {gene}').strip()
    print(f'GENE {gene}')
    print(response)