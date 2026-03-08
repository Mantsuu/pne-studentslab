from pathlib import Path

filename = Path('SEQUENCES/ADA.txt')

contents = filename.read_text()

lines = contents.split('\n')

body = lines[1:]

join_body = ''.join(body)

print(len(join_body))