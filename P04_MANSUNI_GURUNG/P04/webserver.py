import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    lines = req.split('\n')
    req_line = lines[0]
    print("Request line: ", end="")
    termcolor.cprint(req_line, "yellow")

    parts = req_line.split(' ')
    if len(parts) > 1:
        path = parts[1].strip()
    else:
        path = ''

    if path == '/':
        try:
            with open('html/index.html', 'r') as f:
                body = f.read()
            status_line = "HTTP/1.1 200 OK\n"
        except FileNotFoundError:
            body = 'Error: index.html not found'
            status_line = "HTTP/1.1 404 NOT FOUND\n"
    elif path == '/info/A' or path == '/info/C' or path == '/info/G' or path == '/info/T':
        try:
            base = path[-1]
            with open(f'html/info/{base}.html', 'r') as f:
                body = f.read()
            status_line = "HTTP/1.1 200 OK\n"
        except FileNotFoundError:
            body = f'Error: {path[-1]}.html not found'
            status_line = "HTTP/1.1 404 NOT FOUND\n"
    else:
        try:
            with open('error.html', 'r') as f:
                body = f.read()
            status_line = "HTTP/1.1 404 NOT FOUND\n"
        except FileNotFoundError:
            body = 'Error: error.html not found'
            status_line = "HTTP/1.1 404 NOT FOUND\n"

    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"

    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())



ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()

print("server configured!")

while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:

        process_client(cs)

        cs.close()
