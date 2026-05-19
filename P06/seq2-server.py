import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j
from Seq1 import Seq

def read_html_file(filename):
    contents = Path(f'html/{filename}').read_text()
    contents = j.Template(contents)
    return contents

def read_gene_file(name):
    try:
        filename = f'sequences2/{name}.txt'
        with open(filename, 'r') as f:
            content = f.read().strip()
        lines = content.split('\n')
        seq_lines = []
        for line in lines:
            line = line.strip()
            if line:
                if line[0] != '>':
                    seq_lines.append(line)
        seq = ''.join(seq_lines)
        return seq
    except FileNotFoundError:
        return None

PORT = 8081


FOLDER ='sequences2/'
GENES = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']

sequences = [
    'ACCTGGTTTACGTTCTAGGGAGTCGTAGCTAGCTACGTAATAG',
    'CCCCTAGCCCAAAAAAAAAAAATGTCCGAAAAATGGGGGGGGG',
    'AAAAAGCTGATGGGGTTCGGCGCGAGCGGCTCGATGCTTTCCG',
    'GGCTAGAGATTCGCGTTTTTTCGCGATGCGCCCCTGGGGAAAG',
    'GTAGATAGATCGCTCCGTAGCTCGCATCGATCGACTACCGACT'
]

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print(arguments)

        if path == "/ping":
            status = 200
            content = Path('html/ping_ok.html').read_text()

        elif path == "/get":
            if 'sequence' in arguments:
                num = arguments['sequence'][0]
                try:
                    index = int(num)
                    if 0 <= index < len(sequences):
                        status = 200
                        content = read_html_file('get.html').render(NUMBER=index, SEQUENCE=sequences[index])
                    else:
                        status = 404
                        content = read_html_file('error.html').render(ERROR=f'Index out of range(0-{len(sequences)-1})')
                except (IndexError, ValueError):
                    status = 404
                    content = read_html_file('error.html').render(ERROR=f'Invalid number: {num}')
            else:
                status = 404
                content = read_html_file('error.html').render(ERROR=f'No sequence selected')
        elif path == "/gene":
            if 'gene' in arguments:
                name = arguments['gene'][0]
                if name in GENES:
                    gene_seq = read_gene_file(name)
                    if gene_seq:
                        status = 200
                        content = read_html_file('gene.html').render(NAME=name, GENE=gene_seq)
                    else:
                        status = 404
                        content = read_html_file('error.html').render(ERROR=f'Could not read gene {name}')
                else:
                    status = 404
                    content = read_html_file('error.html').render(ERROR=f'Gene {name} not found')
        elif path == "/operation":
            if 'msg' in arguments and 'op' in arguments:
                sequence = arguments['msg'][0].upper()
                operation = arguments['op'][0]
                if not sequence:
                    status = 404
                    content = read_html_file('error.html').render(ERROR=f'No sequence provided')
                else:
                    s = Seq(sequence)
                    if operation == 'info':
                        total = s.len()
                        counts = s.count()
                        result = f'Total length: {total} <br>'
                        for base in ['A', 'C', 'T', 'G']:
                            count = counts.get(base, 0)
                            if total > 0:
                                percentage = (count/total) * 100
                                result += f'{base}: {count} ({percentage:.1f}%)<br>'
                            else:
                                result += f'{base}: {count} (0,0%)<br>'
                        status = 200
                        content = read_html_file('operation.html').render(SEQUENCE=sequence, OPERATION='info', RESULT=result)
                    elif operation == 'comp':
                        complement = s.complement()
                        status =200
                        content = read_html_file('operation.html').render(SEQUENCE=sequence, OPERATION='comp', RESULT=complement)
                    elif operation == 'rev':
                        reverse = s.reverse()
                        status =200
                        content = read_html_file('operation.html').render(SEQUENCE=sequence, OPERATION='rev', RESULT=reverse)
                    else:
                        status = 404
                        content = read_html_file('error.html').render(ERROR=f'unknown operation')
            else:
                status = 404
                content = read_html_file('error.html').render(ERROR=f'No sequence or operation selected')

        elif path == "/":
            status = 200
            content = Path('html/index.html').read_text()
        else:
            status = 404
            content = Path('html/error.html').read_text()

        self.send_response(status)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(content))

        return



Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
