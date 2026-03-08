from pathlib import Path

FILENAME = "SEQUENCES/RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

lines = file_contents.split('\n')

print(lines[0])
