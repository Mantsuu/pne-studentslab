from Seq1 import Seq

print('----| Practice 1, Exercise 7 |----')

sequences = [Seq(), Seq('ACTGA'), Seq('Invalid sequence')]

for i, seq in enumerate(sequences):
    print(f'Sequence {i}: (Length: {seq.len()}) {seq}')
    print(f'Bases: {seq.count()}')
    print(f'Rev: {seq.reverse()}')

