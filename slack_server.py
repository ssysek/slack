import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from .requests import get_all


hostPort = 88


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        full_path = urlparse(self.path)
        path = full_path.path
        qs = parse_qs(full_path.query)

        '''example request'''
        if path == "/fixtures":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(requests.get_all(), "utf-8"))

        else:
            pass


    def do_POST(self):

        full_path = urlparse(self.path)
        path = full_path.path
        qs = parse_qs(full_path.query)


myServer = HTTPServer(('', hostPort), MyServer)
print(time.asctime(), "Server Slack Starts - %s:%s" % ('', hostPort))

try:
    myServer.serve_forever()

except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % ('', hostPort))