class Seq:
    def __init__(self, strbases, name=""):
        valid_bases = ['A', 'C', 'T', 'G']
        self.strbases = strbases

        for base in strbases:
            if base not in valid_bases:
                self.strbases = 'ERROR'
                print('ERROR')
                return
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f'Sequence {i}: (Length: {seq.len()}) {seq}')

def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        seq_list.append(Seq(pattern * i))
    return seq_list

seq_list1 = generate_seqs('A', 3)
seq_list2 = generate_seqs('AC', 5)

print('List 1:')
print_seqs(seq_list1)
print('List 2:')
print_seqs(seq_list2)

