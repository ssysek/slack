import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from requests_on_REST.delete_user import delete_user
from requests_on_REST.get_all_users import get_all_users
from requests_on_REST.get_user_by_id import get_user_by_id_param
from io import BytesIO

from requests_on_REST.register import register

HOST_PORT = 86


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        full_path = urlparse(self.path)
        path = full_path.path
        qs = parse_qs(full_path.query)

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

        if path == "/user_id":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(get_user_by_id_param(qs).to_json(orient='records',
                                                                    date_format='iso'),
                                   "utf-8"))

        if path == "/register":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            register(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())

        if path == "/delete_user":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            self.send_response(200)
            self.end_headers()
            delete_user(body)
            response = BytesIO()
            self.wfile.write(response.getvalue())
        else:
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("POST RECEIVED", "utf-8"))


def connection():

    my_server = HTTPServer(('', HOST_PORT), MyServer)
    print(time.asctime(), "Server Slack Starts - %s:%s" % ('', HOST_PORT))

    try:
        my_server.serve_forever()

    except KeyboardInterrupt:
        pass

    my_server.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % ('', HOST_PORT))


if __name__ == '__main__':
    connection()
