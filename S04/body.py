from pathlib import Path

filename = Path('SEQUENCES/U5.txt')

contents = filename.read_text()

lines = contents.split('\n')

body = lines[1:]

print('\n'.join(body))
