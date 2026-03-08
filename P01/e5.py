from Seq1 import Seq

print('----| Practice 1, Exercise 5 |----')

sequences = [Seq(), Seq('ACTGA'), Seq('Invalid sequence')]

for i, seq in enumerate(sequences):
    print(f'Sequence {i}: (Length: {seq.len()}) {seq}')
    a_count = seq.count_bases('A')
    c_count = seq.count_bases('C')
    t_count = seq.count_bases('T')
    g_count = seq.count_bases('G')
    print(f'A: {a_count}, C: {c_count}, T: {t_count}, G: {g_count}')


