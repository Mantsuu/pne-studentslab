from pathlib import Path

def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    file_path = Path(filename)
    contents = file_path.read_text()
    lines = contents.split('\n')
    seq_lines = []
    for line in lines:
        if line and not line.startswith('>'):
            seq_lines.append(line.strip())
    sequence = ''.join(seq_lines)
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    count = 0
    for charac in seq:
        if charac in base:
            count += 1
    return count

def seq_count(seq):
    bases = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in seq:
        if base in bases:
            bases[base] += 1
    return bases

def seq_reverse(seq, n):
    fragment = seq[:n]
    reverse = fragment[::-1]
    return reverse

def seq_complement(seq):
    complement_dict= {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    complement = ''
    for base in seq:
        complement += complement_dict.get(base, base)
    return complement