import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from requests_on_REST.get_all_users import get_all_users
from requests_on_REST.get_user_by_id import get_user_by_id_param

hostPort = 86


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        full_path = urlparse(self.path)
        path = full_path.path
        qs = parse_qs(full_path.query)

        '''example request'''
        '''http://localhost:86/all_users'''
        if path == "/all_users":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(get_all_users(), "utf-8"))

        else:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("Hello World!! - GET RECEIVED", "utf-8"))

    def do_POST(self):
        full_path = urlparse(self.path)
        path = full_path.path
        qs = parse_qs(full_path.query)

        if path == '/user_id':
            '''http://localhost:86/user_id?user_id=10'''
            content_length = int(self.headers['Content-Length'])  # Gets the size of data
            post_data = self.rfile.read(content_length)  # Gets the data itself
            result = get_user_by_id_param(post_data)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(result, "utf-8"))

        else:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("POST RECEIVED", "utf-8"))


myServer = HTTPServer(('', hostPort), MyServer)
print(time.asctime(), "Server Slack Starts - %s:%s" % ('', hostPort))

try:
    myServer.serve_forever()

except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % ('', hostPort))
