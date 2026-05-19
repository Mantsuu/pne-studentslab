import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import jinja2 as j
import json
import http.client
from Seq1 import Seq

PORT = 8081

SERVER = 'rest.ensembl.org'
PARAMS = '?content-type=application/json'


def read_html_file(filename):
    filepath = Path(f'html/{filename}')
    contents = filepath.read_text(encoding='utf-8')
    return j.Template(contents)


def is_json(arguments):
    return arguments.get('json', [None])[0] == '1'


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/listSpecies":

            limit = arguments.get('limit', [None])[0]

            conn = http.client.HTTPConnection(SERVER)
            conn.request('GET', '/info/species' + PARAMS)
            r1 = conn.getresponse()

            if r1.status == 200:
                data = json.loads(r1.read().decode())
            else:
                data = None

            conn.close()

            if data and 'species' in data:

                species_list = []
                for s in data['species']:
                    if s.get('display_name'):
                        species_list.append(s['display_name'])

                total = len(species_list)

                if limit and limit.isdigit():
                    species_list = species_list[:int(limit)]
                    limit_use = int(limit)
                else:
                    limit_use = 'all'

                if is_json(arguments):
                    status = 200
                    content = json.dumps({
                        "total": total,
                        "limit": limit_use,
                        "species": species_list
                    })
                else:
                    status = 200
                    content = read_html_file('listSpecies.html').render(
                        TOTAL=total,
                        LIMIT=limit_use,
                        SPECIES_LIST=species_list
                    )

            else:
                status = 404
                content = json.dumps({"error": "No species data"}) if is_json(arguments) else \
                    read_html_file('error.html').render(ERROR='No species data')


        elif path == "/karyotype":

            species = arguments.get('species', [None])[0]

            conn = http.client.HTTPConnection(SERVER)
            conn.request('GET', f'/info/assembly/{species}{PARAMS}')
            r1 = conn.getresponse()

            if r1.status == 200:
                data = json.loads(r1.read().decode())
            else:
                data = None

            conn.close()

            if data and 'karyotype' in data:

                chromosomes = data['karyotype']

                if chromosomes:

                    if is_json(arguments):
                        status = 200
                        content = json.dumps({
                            "species": species,
                            "karyotype": chromosomes
                        })
                    else:
                        status = 200
                        content = read_html_file('karyotype.html').render(
                            SPECIES=species,
                            CHROMOSOMES=chromosomes
                        )

                else:
                    status = 404
                    content = json.dumps({"error": "No chromosomes"}) if is_json(arguments) else \
                        read_html_file('error.html').render(ERROR='No chromosomes found')

            else:
                status = 404
                content = json.dumps({"error": "Species not found"}) if is_json(arguments) else \
                    read_html_file('error.html').render(ERROR='Species not found')


        elif path == "/chromosomeLength":

            species = arguments.get('species', [None])[0]
            chromo = arguments.get('chromo', [None])[0]

            conn = http.client.HTTPConnection(SERVER)
            conn.request('GET', f'/info/assembly/{species}{PARAMS}')
            r1 = conn.getresponse()

            if r1.status == 200:
                data = json.loads(r1.read().decode())
            else:
                data = None

            conn.close()

            if data and 'top_level_region' in data:

                length = None
                for r in data['top_level_region']:
                    if r.get('name') == chromo:
                        length = r.get('length')

                if length is not None:

                    if is_json(arguments):
                        status = 200
                        content = json.dumps({
                            "species": species,
                            "chromosome": chromo,
                            "length": length
                        })
                    else:
                        status = 200
                        content = read_html_file('chromosomeLength.html').render(
                            SPECIES=species,
                            CHROMO=chromo,
                            LENGTH=length
                        )

                else:
                    status = 404
                    content = json.dumps({"error": "chromosome not found"}) if is_json(arguments) else \
                        read_html_file('error.html').render(ERROR='chromosome not found')

            else:
                status = 404
                content = json.dumps({"error": "species not found"}) if is_json(arguments) else \
                    read_html_file('error.html').render(ERROR='species not found')


        elif path == "/geneLookup":

            gene = arguments.get('gene', [None])[0]

            conn = http.client.HTTPConnection(SERVER)
            conn.request('GET', f'/xrefs/symbol/homo_sapiens/{gene.upper()}{PARAMS}')
            r1 = conn.getresponse()

            data = json.loads(r1.read().decode()) if r1.status == 200 else None
            conn.close()

            gene_id = None
            if data and len(data) > 0:
                gene_id = data[0].get('id')

            if gene_id:

                if is_json(arguments):
                    status = 200
                    content = json.dumps({
                        "gene": gene.upper(),
                        "gene_id": gene_id
                    })
                else:
                    status = 200
                    content = read_html_file('genelookup.html').render(
                        GENE=gene.upper(),
                        GENE_ID=gene_id
                    )

            else:
                status = 404
                content = json.dumps({"error": "gene not found"}) if is_json(arguments) else \
                    read_html_file('error.html').render(ERROR='gene not found')


        elif path == "/geneSeq":

            gene = arguments.get('gene', [None])[0]

            conn = http.client.HTTPConnection(SERVER)
            conn.request('GET', f'/xrefs/symbol/homo_sapiens/{gene.upper()}{PARAMS}')
            r1 = conn.getresponse()

            data = json.loads(r1.read().decode()) if r1.status == 200 else None
            conn.close()

            gene_id = None
            if data and len(data) > 0:
                gene_id = data[0].get('id')

            if gene_id:

                conn = http.client.HTTPConnection(SERVER)
                conn.request('GET', f'/sequence/id/{gene_id}{PARAMS}')
                r1 = conn.getresponse()

                seq_data = json.loads(r1.read().decode()) if r1.status == 200 else None
                conn.close()

                if seq_data and 'seq' in seq_data:

                    sequence = seq_data['seq']

                    if is_json(arguments):
                        status = 200
                        content = json.dumps({
                            "gene": gene.upper(),
                            "sequence": sequence
                        })
                    else:
                        status = 200
                        content = read_html_file('gene_seq.html').render(
                            GENE=gene.upper(),
                            SEQUENCE=sequence
                        )

                else:
                    status = 404
                    content = json.dumps({"error": "sequence not found"}) if is_json(arguments) else \
                        read_html_file('error.html').render(ERROR='sequence not found')

            else:
                status = 404
                content = json.dumps({"error": "gene not found"}) if is_json(arguments) else \
                    read_html_file('error.html').render(ERROR='gene not found')


        elif path == "/geneInfo":

            gene = arguments.get('gene', [None])[0]

            conn = http.client.HTTPConnection(SERVER)
            conn.request('GET', f'/xrefs/symbol/homo_sapiens/{gene.upper()}{PARAMS}')
            r1 = conn.getresponse()

            data = json.loads(r1.read().decode()) if r1.status == 200 else None
            conn.close()

            gene_id = None
            if data and len(data) > 0:
                gene_id = data[0].get('id')

            if gene_id:

                conn = http.client.HTTPConnection(SERVER)
                conn.request('GET', f'/lookup/id/{gene_id}{PARAMS}')
                r1 = conn.getresponse()

                info = json.loads(r1.read().decode()) if r1.status == 200 else None
                conn.close()

                if info:

                    if is_json(arguments):
                        status = 200
                        content = json.dumps(info)
                    else:
                        status = 200
                        content = read_html_file('gene_info.html').render(
                            GENE=gene.upper(),
                            GENE_ID=info.get('id'),
                            DESCRIPTION=info.get('description'),
                            CHROMOSOME=info.get('seq_region_name'),
                            START=info.get('start'),
                            END=info.get('end'),
                            STRAND=info.get('strand'),
                            BIOTYPE=info.get('biotype')
                        )

                else:
                    status = 404
                    content = json.dumps({"error": "gene info not found"}) if is_json(arguments) else \
                        read_html_file('error.html').render(ERROR='gene info not found')

            else:
                status = 404
                content = json.dumps({"error": "gene not found"}) if is_json(arguments) else \
                    read_html_file('error.html').render(ERROR='gene not found')


        elif path == "/geneCalc":

            gene = arguments.get('gene', [None])[0]

            conn = http.client.HTTPConnection(SERVER)
            conn.request('GET', f'/xrefs/symbol/homo_sapiens/{gene.upper()}{PARAMS}')
            r1 = conn.getresponse()

            data = json.loads(r1.read().decode()) if r1.status == 200 else None
            conn.close()

            gene_id = None
            if data and len(data) > 0:
                gene_id = data[0].get('id')

            if gene_id:

                conn = http.client.HTTPConnection(SERVER)
                conn.request('GET', f'/sequence/id/{gene_id}{PARAMS}')
                r1 = conn.getresponse()

                seq_data = json.loads(r1.read().decode()) if r1.status == 200 else None
                conn.close()

                if seq_data and 'seq' in seq_data:

                    s = Seq(seq_data['seq'])
                    total = s.len()
                    counts = s.count()

                    if is_json(arguments):
                        status = 200
                        content = json.dumps({
                            "gene": gene.upper(),
                            "length": total,
                            "counts": counts
                        })
                    else:
                        status = 200
                        content = read_html_file('gene_calc.html').render(
                            GENE=gene.upper(),
                            TOTAL_LENGTH=total,
                            COUNTS=counts
                        )

                else:
                    status = 404
                    content = json.dumps({"error": "sequence not found"}) if is_json(arguments) else \
                        read_html_file('error.html').render(ERROR='sequence not found')

            else:
                status = 404
                content = json.dumps({"error": "gene not found"}) if is_json(arguments) else \
                    read_html_file('error.html').render(ERROR='gene not found')


        elif path == "/geneList":

            chromo = arguments.get('chromo', [None])[0]
            start = arguments.get('start', [None])[0]
            end = arguments.get('end', [None])[0]

            conn = http.client.HTTPConnection(SERVER)
            conn.request('GET', f'/overlap/region/human/{chromo}:{start}-{end}{PARAMS}')
            r1 = conn.getresponse()

            data = json.loads(r1.read().decode()) if r1.status == 200 else None
            conn.close()

            genes = []
            if data:
                for e in data:
                    if e.get('display_name'):
                        genes.append(e['display_name'])

            if is_json(arguments):
                status = 200
                content = json.dumps({
                    "chromosome": chromo,
                    "start": start,
                    "end": end,
                    "genes": genes,
                    "count": len(genes)
                })
            else:
                status = 200
                content = read_html_file('gene_list.html').render(
                    CHROMO=chromo,
                    START=start,
                    END=end,
                    GENES=genes,
                    COUNT=len(genes)
                )

        elif path == "/":

            status = 200
            content = Path('html/index.html').read_text(encoding='utf-8')


        else:
            status = 404
            content = json.dumps({"error": "not found"}) if is_json(arguments) else \
                read_html_file('error.html').render(ERROR='not found')

        self.send_response(status)
        self.send_header('Content-Type', 'application/json' if is_json(arguments) else 'text/html')
        self.end_headers()
        self.wfile.write(content.encode())


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at {PORT}")
    httpd.serve_forever()




