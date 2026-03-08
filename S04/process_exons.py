from pathlib import Path

def get_exons_from_file(filename):
    filename = Path('SEQUENCES/APOE_EXONS.txt')
    contents = filename.read_text()
    lines = contents.split('\n')

    exons = []
    current = []

    for line in lines:
        if line.startswith('>'):
            if current:
                exons.append(''.join(current))
                current = []
        else:
            if line.strip():
                current.append(line.strip())
    if current:
        exons.append(''.join(current))
    return exons

apoe_exons = get_exons_from_file("APOE_EXONS.txt")
print(apoe_exons)