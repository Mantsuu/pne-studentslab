import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        request_path = self.path

        if request_path == '/' or request_path == '/index.html':
            file_path = Path('html/index.html')

        elif request_path == '/info/A' or request_path == '/info/A.html':
            file_path = Path('html/info/A.html')

        elif request_path == '/info/C' or request_path == '/info/C.html':
            file_path = Path('html/info/C.html')

        elif request_path == '/info/G' or request_path == '/info/G.html':
            file_path = Path('html/info/G.html')

        elif request_path == '/info/T' or request_path == '/info/T.html':
            file_path = Path('html/info/T.html')
        else:
            file_path = Path('html/error.html')

        try:
            with open(file_path, 'r') as f:
                contents = f.read()

            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())
        except FileNotFoundError:
            error_contents = f'Error: {file_path} not found'
            self.send_response(404)  # -- Status line: OK!
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(error_contents.encode()))
            self.end_headers()
            self.wfile.write(error_contents.encode())
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
