import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            file_request = 'index.html'
        else:
            file_request = self.path[1:]

        file_path = Path(file_request)

        try:
            with open(file_path, 'r') as f:
                contents = f.read()

            if file_path.suffix == '.html':
                content_type = 'text/html'
            elif file_path.suffix == '.css':
                content_type = 'text/css'
            elif file_path.suffix == '.js':
                content_type = 'application/javascript'
            else:
                content_type = 'text/plain'

            self.send_response(200)  # -- Status line: OK!
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())
        except FileNotFoundError:
            try:
                error_path = Path('error.html')
                with open(error_path, 'r') as f:
                    error_contents = f.read()
                self.send_response(404)  # -- Status line: OK!
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(error_contents.encode()))
                self.end_headers()
                self.wfile.write(error_contents.encode())
            except FileNotFoundError:
                error_contents = 'Resource not available'
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
