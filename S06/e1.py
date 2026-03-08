class Seq:
    def __init__(self, strbases, name=""):
        valid_bases = ['A','C', 'T', 'G']
        self.strbases = strbases

        for base in strbases:
            if base not in valid_bases:
                self.strbases = 'ERROR'
                print('ERROR')
                return
        print("New sequence created!")

    def __str__(self):
        return self.strbases

s1 = Seq("ACCTG")
s2 = Seq('Hello? Am i a valid sequence?')
print(f'Sequence 1: {s1}')
print(f'Sequence 2: {s2}')

