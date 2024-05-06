import os
import argparse
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(
    server_class=HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
    port=8888,
    directory=None
):
    if directory:
        os.chdir(directory) # Change the current working directory is dierectory is specified
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(F"Serving HTTP on http://locahost:{port} from directory {directory} ...")
    httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HTTP Server")
    parser.add_argument("--dir", type=str, help="The directory to serve files from", default=".")
    parser.add_argument("--port", type=int, help="The port to listen on", default=8888)
    args = parser.parse_args()

    run(directory=args.dir, port=args.port)