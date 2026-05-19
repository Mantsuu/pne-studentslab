from pathlib import Path

class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            self.strbases = 'NULL'
            print("Null sequence created")
            return

        valid_bases = ['A','C', 'T', 'G']
        self.strbases = strbases

        for base in strbases:
            if base not in valid_bases:
                self.strbases = 'ERROR'
                print('INVALID sequence')
                return
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == 'NULL' or self.strbases == 'ERROR':
            return 0
        return len(self.strbases)

    def count_bases(self, base):
        if self.strbases == 'NULL' or self.strbases == 'ERROR':
            return 0
        return self.strbases.count(base)

    def count(self):
        bases = ['A', 'C', 'T', 'G']
        counts = {}
        for base in bases:
            counts[base] = self.count_bases(base)
        return counts

    def reverse(self):
        if self.strbases == 'NULL' or self.strbases == 'ERROR':
            return self.strbases
        return self.strbases[::-1]

    def complement(self):
        if self.strbases == 'NULL' or self.strbases == 'ERROR':
            return self.strbases
        complement_dict = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C'
        }
        result = ''
        for base in self.strbases:
            result += complement_dict[base]
        return result

    def read_fasta(self, filename):
        file_path = Path(filename)
        contents = file_path.read_text()
        lines = contents.split('\n')
        seq_lines = []
        for line in lines:
            if line and not line.startswith('>'):
                seq_lines.append(line.strip())
        sequence = ''.join(seq_lines)
        self.strbases = sequence

